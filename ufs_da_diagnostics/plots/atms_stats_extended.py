"""
Extended ATMS Channel‑Wise OMB/OMA Statistics
=============================================

This module computes an extended set of per‑channel OMB/OMA diagnostics
for ATMS radiance observations using QC2 filtering. It expands upon the
basic ATMS statistics by including:

- Mean OMB / OMA
- Standard deviation OMB / OMA
- RMS OMB / OMA
- RMS difference (OMA – OMB)
- Normalized RMS (NRMS)
- Bias‑corrected RMS (BC‑RMS)

The output is a **4‑panel diagnostic figure**:

1. Mean & Std (dual y‑axes)
2. RMS
3. RMS Difference
4. Normalized RMS & Bias‑Corrected RMS

Channel groups (Window, O₂, H₂O) are shaded for interpretability.

Output
------
A single PNG file:

    <label>_stats_extended.png

saved in the specified output directory.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from .utils_loaders import load_omb, load_oma_explicit, load_qc_universal


# ---------------------------------------------------------------------
# Correct ATMS channel groups
# ---------------------------------------------------------------------
def channel_groups():
    """
    Return ATMS channel group definitions for shading and legends.

    Returns
    -------
    list of tuples
        Each tuple contains:
        (group_name, start_channel, end_channel, color)

    Notes
    -----
    ATMS channel grouping:

    - Window: channels 1–2 and 16–17
    - O₂ Temperature: channels 3–15
    - H₂O: channels 18–22
    """
    return [
        ("Window", 1, 2, "lightgrey"),
        ("O₂ Temp", 3, 15, "lightblue"),
        ("Window", 16, 17, "lightgrey"),
        ("H₂O", 18, 22, "lightgreen"),
    ]


# ---------------------------------------------------------------------
# Extended ATMS Stats
# ---------------------------------------------------------------------
def plot_stats_atms_extended(f, varname, label, outdir):
    """
    Plot extended ATMS per‑channel OMB/OMA diagnostics (QC2‑filtered).

    This function computes and visualizes an extended suite of
    per‑channel statistics:

    - Mean OMB / OMA
    - Std  OMB / OMA
    - RMS  OMB / OMA
    - RMS difference (OMA – OMB)
    - Normalized RMS (NRMS = RMS / Std)
    - Bias‑corrected RMS (BC‑RMS = Std)

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
    - One PNG file is produced containing all four panels.

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
        print(f"[SKIP] {label} ATMS extended stats: missing OMB/OMA")
        return

    # Broadcast QC if needed
    if qc.ndim == 1:
        qc = np.repeat(qc[:, None], omb.shape[1], axis=1)

    nchan = omb.shape[1]
    chans = np.arange(1, nchan + 1)

    # Allocate arrays
    mean_omb = np.full(nchan, np.nan)
    mean_oma = np.full(nchan, np.nan)
    std_omb = np.full(nchan, np.nan)
    std_oma = np.full(nchan, np.nan)
    rms_omb = np.full(nchan, np.nan)
    rms_oma = np.full(nchan, np.nan)
    rms_diff = np.full(nchan, np.nan)
    nrms_omb = np.full(nchan, np.nan)
    nrms_oma = np.full(nchan, np.nan)
    bc_rms_omb = np.full(nchan, np.nan)
    bc_rms_oma = np.full(nchan, np.nan)

    # -----------------------------------------------------------------
    # Compute stats per channel
    # -----------------------------------------------------------------
    for ch in range(nchan):
        mask = (qc[:, ch] == 0) & np.isfinite(omb[:, ch]) & np.isfinite(oma[:, ch])
        if not np.any(mask):
            continue

        o = omb[mask, ch].astype("float64")
        a = oma[mask, ch].astype("float64")

        mean_omb[ch] = np.mean(o)
        mean_oma[ch] = np.mean(a)

        std_omb[ch] = np.nanstd(o, ddof=1)
        std_oma[ch] = np.nanstd(a, ddof=1)

        rms_omb[ch] = np.sqrt(np.mean(o**2))
        rms_oma[ch] = np.sqrt(np.mean(a**2))

        rms_diff[ch] = rms_oma[ch] - rms_omb[ch]

        nrms_omb[ch] = rms_omb[ch] / std_omb[ch] if std_omb[ch] > 0 else np.nan
        nrms_oma[ch] = rms_oma[ch] / std_oma[ch] if std_oma[ch] > 0 else np.nan

        bc_rms_omb[ch] = std_omb[ch]
        bc_rms_oma[ch] = std_oma[ch]

    # -----------------------------------------------------------------
    # Plotting
    # -----------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)

    ax_meanstd = axes[0, 0]
    ax_rms = axes[0, 1]
    ax_rmsdiff = axes[1, 0]
    ax_norm = axes[1, 1]

    # Shading helper
    def shade(ax):
        for name, c1, c2, color in channel_groups():
            ax.axvspan(c1 - 0.5, c2 + 0.5, color=color, alpha=0.25, zorder=0)
    
    # -------------------------
    # Panel 1: Mean & Std
    # -------------------------
    shade(ax_meanstd)

    ax_meanstd.plot(chans, mean_omb, "o-", color="blue", label="Mean OMB")
    ax_meanstd.plot(chans, mean_oma, "o-", color="red", label="Mean OMA")
    ax_meanstd.set_ylabel("Mean")

    ax_std = ax_meanstd.twinx()
    ax_std.plot(chans, std_omb, "s--", color="orange", label="Std OMB")
    ax_std.plot(chans, std_oma, "s--", color="purple", label="Std OMA")
    ax_std.set_ylabel("Std")
    
    ax_meanstd.set_title("Mean & Std (OMB / OMA)")
    ax_meanstd.set_xlabel("Channel")
    
    # Combined legend
    lines1, labels1 = ax_meanstd.get_legend_handles_labels()
    lines2, labels2 = ax_std.get_legend_handles_labels()
    leg1 = ax_meanstd.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc="lower left",
        fontsize=8,
        frameon=True
    )
    ax_meanstd.add_artist(leg1)

    # Channel-group legend
    ax_meanstd.legend(
        handles=[
            Patch(facecolor="lightgrey", label="Window (1–2, 16–17)"),
            Patch(facecolor="lightblue", label="O₂ Temp (3–15)"),
            Patch(facecolor="lightgreen", label="H₂O (18–22)")
        ],
        loc="lower right",
        fontsize=6,
        frameon=True
    )
   
    # -------------------------
    # Panel 2: RMS
    # -------------------------
    shade(ax_rms)
    ax_rms.plot(chans, rms_omb, "^-", color="black", label="RMS OMB")
    ax_rms.plot(chans, rms_oma, "^-", color="magenta", label="RMS OMA")
    ax_rms.set_title("RMS (OMB / OMA)")
    ax_rms.set_xlabel("Channel")
    ax_rms.set_ylabel("RMS")
    ax_rms.legend(loc="upper left", fontsize=8)

    # -------------------------
    # Panel 3: RMS Difference
    # -------------------------
    shade(ax_rmsdiff)
    ax_rmsdiff.plot(chans, rms_diff, "o-", color="green", label="RMS(OMA) – RMS(OMB)")
    ax_rmsdiff.set_title("RMS Difference (OMA – OMB)")
    ax_rmsdiff.set_xlabel("Channel")
    ax_rmsdiff.set_ylabel("Difference")
    ax_rmsdiff.legend(loc="lower left", fontsize=8)
    
    # -------------------------
    # Panel 4: Normalized + BC RMS
    # -------------------------
    shade(ax_norm)

    ax_norm.plot(chans, nrms_omb, "^-", color="black", label="NRMS OMB")
    ax_norm.plot(chans, nrms_oma, "^-", color="magenta", label="NRMS OMA")
    ax_norm.plot(chans, bc_rms_omb, "s--", color="orange", label="BC-RMS OMB")
    ax_norm.plot(chans, bc_rms_oma, "s--", color="purple", label="BC-RMS OMA")

    ax_norm.set_title("Normalized RMS & Bias-Corrected RMS")
    ax_norm.set_xlabel("Channel")
    ax_norm.set_ylabel("RMS")

    # Unified y-axis scaling
    all_vals = np.concatenate([
        nrms_omb, nrms_oma,
        bc_rms_omb, bc_rms_oma
    ])
    all_vals = all_vals[np.isfinite(all_vals)]
    ymin, ymax = np.min(all_vals), np.max(all_vals)
    yr = ymax - ymin
    ax_norm.set_ylim(ymin - 0.1 * yr, ymax + 0.1 * yr)

    ax_norm.legend(loc="upper right", fontsize=8)

    # -----------------------------------------------------------------
    # Title
    # -----------------------------------------------------------------
    fig.suptitle(
        f"{label} Extended OMB/OMA Stats (QC2==0)",
        fontsize=13,
        y=1.02
    )

    # Save
    outpath = os.path.join(outdir, f"{label.lower()}_stats_extended.png")
    fig.savefig(outpath, dpi=150)
    plt.close(fig)
    print(f"[SAVED] {outpath}")
