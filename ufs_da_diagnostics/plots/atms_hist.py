#!/usr/bin/env python3
"""
ATMS Per‑Channel Histograms
===========================

This module generates per‑channel histograms for ATMS radiance
observations using the same logic as the original
``obs_diag_plots.py`` implementation.

The workflow:

1. Load QC2 flags, OMB, and OMA for an ATMS variable
2. Apply QC2==0 mask (assimilated observations only)
3. Compute adaptive histogram bins based on OMB standard deviation
4. Plot:
   - Grey histogram of OMB
   - KDE of OMB (dimgray)
   - KDE of OMA (red)
5. Annotate assimilated count
6. Save one PNG per channel

This module is used by the observation diagnostics subsystem and is
typically invoked indirectly through higher‑level plot orchestrators.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from .utils_loaders import load_qc_any, load_omb, load_oma_explicit
from .utils_common import annotate_assimilated


def plot_hist_atms(f, varname, label, outdir):
    """
    Plot per‑channel ATMS histograms for a given variable.

    This function reproduces the original ATMS histogram behavior from
    ``obs_diag_plots.py``. For each channel, it plots:

    - Grey histogram of OMB (QC2==0 only)
    - KDE of OMB (dimgray)
    - KDE of OMA (red)
    - Assimilated count annotation

    Adaptive bin counts are selected based on the standard deviation of
    OMB for each channel.

    Parameters
    ----------
    f : xarray.Dataset or dict-like
        Observation diagnostics file handle or structure containing
        OMB, OMA, and QC fields.
    varname : str
        Name of the ATMS variable (e.g., ``"brightness_temperature"``,
        ``"atms_bt"``).
    label : str
        Short label used in plot titles and output filenames.
    outdir : str
        Directory where output PNG files will be written.

    Notes
    -----
    - Only QC2==0 observations are included.
    - If QC2 is missing or not 2‑D, the function prints a skip message.
    - One PNG file is produced per channel.
    - KDE plotting is wrapped in a try/except to avoid failures on
      degenerate distributions.

    Returns
    -------
    None
        PNG files are written to ``outdir``.
    """
    os.makedirs(outdir, exist_ok=True)

    qc2 = load_qc_any(f, varname)
    if qc2 is None or qc2.ndim != 2:
        print(f"[SKIP] {label} hist: not radiance or QC missing")
        return

    omb = load_omb(f, varname)
    oma = load_oma_explicit(f, varname)

    # Ensure 2D
    if omb.ndim == 1:
        omb = omb[:, np.newaxis]
    if oma.ndim == 1:
        oma = oma[:, np.newaxis]

    nlocs, nchans = qc2.shape

    for ch in range(nchans):
        qc_mask = (qc2[:, ch] == 0)
        omb_ch = omb[:, ch]
        oma_ch = oma[:, ch]

        valid_omb = qc_mask & np.isfinite(omb_ch)
        valid_oma = qc_mask & np.isfinite(oma_ch)

        N_OMB = int(np.sum(valid_omb))
        if N_OMB == 0:
            continue

        # Adaptive bins
        std = np.std(omb_ch[valid_omb])
        if std < 0.3:
            nbins = 120
        elif std < 1.0:
            nbins = 100
        else:
            nbins = 80

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.hist(omb_ch[valid_omb], bins=nbins, color="lightgrey",
                edgecolor=None, alpha=0.7, density=True)

        try:
            sns.kdeplot(omb_ch[valid_omb], color="dimgray", linewidth=2, ax=ax)
            sns.kdeplot(oma_ch[valid_oma], color="red", linewidth=2, ax=ax)
        except Exception:
            pass

        fig.suptitle(f"{label} Ch {ch+1} Histogram (QC2==0)", y=0.97, fontsize=12)
        annotate_assimilated(fig, N_OMB)

        ax.set_xlabel("Value")
        ax.set_ylabel("Density")
        ax.grid(True, alpha=0.3)

        fname = os.path.join(outdir, f"{label.lower()}_ch{ch+1:02d}_hist.png")
        fig.tight_layout(rect=[0, 0, 1, 0.97])
        fig.savefig(fname, dpi=150)
        plt.close(fig)
        print(f"[SAVED] {fname}")
