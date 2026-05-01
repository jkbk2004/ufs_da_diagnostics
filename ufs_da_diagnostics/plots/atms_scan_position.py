# ============================================================
# ATMS Scan-Position Diagnostics (QC2-filtered)
# ============================================================

"""
ATMS Scan‑Position Diagnostics
==============================

This module computes scan‑position‑dependent OMB/OMA statistics for
ATMS radiance observations using QC2 filtering. It reproduces the
behavior of the original scan‑position diagnostics from
``obs_diag_plots.py`` but in a modular, maintainable form.

Workflow
--------
1. Load OMB and OMA using loader utilities (supports ombg/oman groups)
2. Load QC flags using ``load_qc_universal`` (Location × Channel)
3. Load scan position and channel number from ``MetaData`` group
4. Broadcast scan position to match QC shape
5. Apply QC2==0 mask and flatten arrays
6. Compute, for each scan position:
   - Mean OMB / OMA
   - Std  OMB / OMA
   - RMS  OMB / OMA
7. Produce a three‑panel figure:
   - Window channels
   - O₂ temperature channels
   - H₂O channels

Output
------
A single PNG file:

    atms_scan_position_qc2.png

saved in the specified output directory.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from .utils_loaders import (
    load_omb,
    load_oma_explicit,
    load_qc_universal,
)

# Channel groups for ATMS
WINDOW_CH = [1, 2, 16, 17]
O2_CH     = list(range(3, 16))
H2O_CH    = list(range(18, 23))


def _compute_stats_by_scan(omb, oma, scanpos, channels, ch_group):
    """
    Compute OMB/OMA statistics grouped by scan position.

    Parameters
    ----------
    omb : numpy.ndarray
        1D array of OMB values after QC filtering.
    oma : numpy.ndarray
        1D array of OMA values after QC filtering.
    scanpos : numpy.ndarray
        1D array of scan positions aligned with ``omb`` and ``oma``.
    channels : numpy.ndarray
        1D array of channel numbers aligned with ``omb`` and ``oma``.
    ch_group : list[int]
        List of channel numbers defining the group (e.g., window, O₂, H₂O).

    Returns
    -------
    scan_positions : numpy.ndarray
        Unique scan positions in ascending order.
    mean_omb : numpy.ndarray
        Mean OMB per scan position.
    mean_oma : numpy.ndarray
        Mean OMA per scan position.
    std_omb : numpy.ndarray
        Standard deviation of OMB per scan position.
    std_oma : numpy.ndarray
        Standard deviation of OMA per scan position.
    rms_omb : numpy.ndarray
        RMS of OMB per scan position.
    rms_oma : numpy.ndarray
        RMS of OMA per scan position.

    Notes
    -----
    - Only observations whose channel is in ``ch_group`` are included.
    - ``np.nanmean`` and ``np.nanstd`` ensure robustness to missing data.
    """
    scan_positions = np.unique(scanpos)
    nscan = len(scan_positions)

    mean_omb = np.zeros(nscan)
    mean_oma = np.zeros(nscan)
    std_omb  = np.zeros(nscan)
    std_oma  = np.zeros(nscan)
    rms_omb  = np.zeros(nscan)
    rms_oma  = np.zeros(nscan)

    for i, sp in enumerate(scan_positions):
        mask = (scanpos == sp) & np.isin(channels, ch_group)

        omb_sp = omb[mask]
        oma_sp = oma[mask]

        mean_omb[i] = np.nanmean(omb_sp)
        mean_oma[i] = np.nanmean(oma_sp)
        std_omb[i]  = np.nanstd(omb_sp)
        std_oma[i]  = np.nanstd(oma_sp)
        rms_omb[i]  = np.sqrt(np.nanmean(omb_sp**2))
        rms_oma[i]  = np.sqrt(np.nanmean(oma_sp**2))

    return scan_positions, mean_omb, mean_oma, std_omb, std_oma, rms_omb, rms_oma


def _plot_panel(ax, scanpos, mean_omb, mean_oma, std_omb, std_oma, rms_omb, rms_oma, title):
    """
    Plot a single scan‑position diagnostics panel.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to draw on.
    scanpos : numpy.ndarray
        Scan positions.
    mean_omb, mean_oma : numpy.ndarray
        Mean OMB/OMA per scan position.
    std_omb, std_oma : numpy.ndarray
        Standard deviation per scan position.
    rms_omb, rms_oma : numpy.ndarray
        RMS per scan position.
    title : str
        Panel title.

    Notes
    -----
    - Mean is plotted on the left y‑axis.
    - Std and RMS are plotted on the right y‑axis.
    """
    ax.plot(scanpos, mean_omb, "o-", color="blue", label="Mean OMB")
    ax.plot(scanpos, mean_oma, "o-", color="red", label="Mean OMA")
    ax.set_ylabel("Mean")

    ax2 = ax.twinx()
    ax2.plot(scanpos, std_omb, "s--", color="orange", label="Std OMB")
    ax2.plot(scanpos, std_oma, "s--", color="purple", label="Std OMA")
    ax2.plot(scanpos, rms_omb, "^-", color="black", label="RMS OMB")
    ax2.plot(scanpos, rms_oma, "^-", color="magenta", label="RMS OMA")
    ax2.set_ylabel("Std / RMS")

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=8)

    ax.set_xlabel("Scan Position")
    ax.set_title(title, loc="left", fontsize=12)


def plot_scan_position_atms(f, var, label, outdir):
    """
    Plot ATMS scan‑position OMB/OMA diagnostics (QC2‑filtered).

    This function generates a three‑panel figure showing scan‑position
    statistics for:

    1. Window channels (1, 2, 16, 17)
    2. O₂ temperature channels (3–15)
    3. H₂O channels (18–22)

    Parameters
    ----------
    f : xarray.Dataset or dict-like
        Observation diagnostics file containing OMB, OMA, QC, and
        ``MetaData/sensorScanPosition`` and ``MetaData/sensorChannelNumber``.
    var : str
        Variable name for ATMS radiances.
    label : str
        Short label used in log messages and output filenames.
    outdir : str
        Directory where the output PNG file will be saved.

    Notes
    -----
    - QC mask is applied per (Location, Channel).
    - Scan position is broadcast to match QC shape before masking.
    - All arrays are flattened after masking.
    - One PNG file is produced containing all three channel groups.

    Returns
    -------
    None
        A single PNG file is written to ``outdir``.
    """
    print("[ATMS] Scan-position diagnostics (QC2-filtered)...")

    os.makedirs(outdir, exist_ok=True)

    # CORRECT: use loader functions (ombg/oman)
    omb = load_omb(f, var)
    oma = load_oma_explicit(f, var)

    if omb is None or oma is None:
        print(f"[SKIP] {label}: missing OMB/OMA for scan-position diagnostics")
        return

    # Load scan-position from MetaData group
    try:
        scanpos = f["MetaData/sensorScanPosition"][:]
    except KeyError:
        raise KeyError("ATMS diag missing MetaData/sensorScanPosition")

    # Load channel numbers from MetaData group
    try:
        channels = f["MetaData/sensorChannelNumber"][:]
    except KeyError:
        raise KeyError("ATMS diag missing MetaData/sensorChannelNumber")
    
    qc = load_qc_universal(f, var)          # (Location, Channel)
    mask = (qc == 0)                        # (Location, Channel)

    # Broadcast scanpos to (Location, Channel) then mask
    scanpos2d = np.broadcast_to(scanpos[:, None], qc.shape)   # (Location, Channel)

    omb = omb[mask]              # 1D: valid (loc, ch)
    oma = oma[mask]              # 1D
    channels = channels[mask]    # 1D
    scanpos = scanpos2d[mask]    # 1D, aligned with omb/oma/channels
    
    fig, axes = plt.subplots(3, 1, figsize=(8, 12), constrained_layout=True)

    sp, momb, moma, stomb, stoma, rmb, rma = _compute_stats_by_scan(
        omb, oma, scanpos, channels, WINDOW_CH
    )
    _plot_panel(axes[0], sp, momb, moma, stomb, stoma, rmb, rma,
                "ATMS Scan-Position — Window Channels (QC2)")

    sp, momb, moma, stomb, stoma, rmb, rma = _compute_stats_by_scan(
        omb, oma, scanpos, channels, O2_CH
    )
    _plot_panel(axes[1], sp, momb, moma, stomb, stoma, rmb, rma,
                "ATMS Scan-Position — O₂ Temperature Channels (QC2)")

    sp, momb, moma, stomb, stoma, rmb, rma = _compute_stats_by_scan(
        omb, oma, scanpos, channels, H2O_CH
    )
    _plot_panel(axes[2], sp, momb, moma, stomb, stoma, rmb, rma,
                "ATMS Scan-Position — H₂O Channels (QC2)")

    outfile = f"{outdir}/atms_scan_position_qc2.png"
    fig.savefig(outfile, dpi=150)
    plt.close(fig)
    print(f"[SAVED] {outfile}")
