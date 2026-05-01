"""
ATMS Channel‑Wise OMB/OMA Statistics
====================================

This module computes per‑channel OMB/OMA mean and standard deviation
for ATMS radiance observations using QC2 filtering. It reproduces the
behavior of the original ATMS channel‑stats diagnostics from
``obs_diag_plots.py`` but in a modular, maintainable form.

Workflow
--------
1. Load OMB and OMA using loader utilities (supports ombg/oman groups)
2. Load QC flags using ``load_qc_universal`` (Location × Channel)
3. For each channel:
   - Apply QC2==0 mask
   - Compute mean OMB / OMA
   - Compute std  OMB / OMA
4. Plot:
   - Mean OMB/OMA (left y‑axis)
   - Std  OMB/OMA (right y‑axis)
   - Shaded channel‑group bands (Window, O₂, H₂O)
   - Combined legend + channel‑group legend

Output
------
A single PNG file:

    <label>_stats.png

saved in the specified output directory.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from .utils_loaders import load_omb, load_oma_explicit, load_qc_universal


def _channel_groups(nchan):
    """
    Define ATMS channel groups for shading and legend.

    Parameters
    ----------
    nchan : int
        Total number of channels.

    Returns
    -------
    dict
        Mapping of group name → (start_channel, end_channel, color).

    Notes
    -----
    Default grouping for 22‑channel ATMS:
    - Window: channels 1–7
    - O₂ temperature: channels 8–16
    - H₂O: channels 17–22
    """
    return {
        "window": (1, 7, "lightgrey"),
        "o2": (8, 16, "lightblue"),
        "h2o": (17, nchan, "lightgreen"),
    }


def plot_stats_atms(f, varname, label, outdir):
    """
    Plot ATMS per‑channel OMB/OMA mean and standard deviation (QC2‑filtered).

    This function computes and plots:
    - Mean OMB / OMA per channel
    - Std  OMB / OMA per channel
    - Shaded channel groups (Window, O₂, H₂O)
    - Combined legend + channel‑group legend

    Parameters
    ----------
    f : xarray.Dataset or dict-like
        Observation diagnostics file containing OMB, OMA, QC, and metadata.
    varname : str
        Variable name for ATMS radiances (e.g., ``"brightness_temperature"``).
    label : str
        Short label used in plot titles and output filenames.
    outdir : str
        Directory where the output PNG file will be saved.

    Notes
    -----
    - QC mask is applied per (Location, Channel).
    - If QC is 1‑D, it is broadcast to match the number of channels.
    - Channels are assumed to be 1‑indexed for plotting.
    - One PNG file is produced.

    Returns
    -------
    None
        A single PNG file is written to ``outdir``.
    """
    os.makedirs(outdir, exist_ok=True)

    omb = load_omb(f, varname)
    oma = load_oma_explicit(f, varname)
    qc = load_qc_universal(f, varname)

    if omb is None or oma is None:
        print(f"[SKIP] {label} ATMS stats: missing OMB/OMA")
        return

    # Broadcast QC if needed
    if qc.ndim == 1:
        qc = np.repeat(qc[:, None], omb.shape[1], axis=1)

    nchan = omb.shape[1]
    chans = np.arange(1, nchan + 1)

    mean_omb = np.full(nchan, np.nan)
    mean_oma = np.full(nchan, np.nan)
    std_omb = np.full(nchan, np.nan)
    std_oma = np.full(nchan, np.nan)

    # Per‑channel statistics
    for ch in range(nchan):
        mask = (qc[:, ch] == 0) & np.isfinite(omb[:, ch]) & np.isfinite(oma[:, ch])
        if np.any(mask):
            mean_omb[ch] = np.mean(omb[mask, ch])
            mean_oma[ch] = np.mean(oma[mask, ch])
            std_omb[ch] = np.std(omb[mask, ch])
            std_oma[ch] = np.std(oma[mask, ch])

    fig, ax1 = plt.subplots(figsize=(7, 4), constrained_layout=True)
    ax2 = ax1.twinx()

    # Shaded channel groups
    groups = _channel_groups(nchan)
    for _, (c1, c2, color) in groups.items():
        ax1.axvspan(c1 - 0.5, c2 + 0.5, color=color, alpha=0.2, zorder=0)

    # Mean
    ax1.plot(chans, mean_omb, "o-", color="blue", label="Mean OMB")
    ax1.plot(chans, mean_oma, "o-", color="red", label="Mean OMA")

    # Std
    ax2.plot(chans, std_omb, "s--", color="orange", label="Std OMB")
    ax2.plot(chans, std_oma, "s--", color="purple", label="Std OMA")

    ax1.set_xlabel("Channel")
    ax1.set_ylabel("Mean")
    ax2.set_ylabel("Std")

    ax1.set_title(f"{label} OMB/OMA Mean/Std (QC2==0)")

    # Combined legend (upper-left)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=8)

    # Channel-group legend (bottom-right)
    group_handles = []
    group_labels = []
    for name, (_, _, color) in groups.items():
        group_handles.append(
            plt.Rectangle((0, 0), 1, 1, color=color, alpha=0.25)
        )
        group_labels.append(
            "Window" if name == "window" else ("O₂ Temp" if name == "o2" else "H₂O")
        )

    ax1.legend(
        group_handles,
        group_labels,
        loc="lower right",
        fontsize=8,
        frameon=True
    )

    outpath = os.path.join(outdir, f"{label.lower()}_stats.png")
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"[SAVED] {outpath}")
