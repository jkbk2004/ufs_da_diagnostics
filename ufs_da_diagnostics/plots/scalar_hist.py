"""
Scalar Observation Histograms

This module provides histogram diagnostics for scalar observation types
(e.g., temperature, humidity, pressure). It supports two modes:

1. Standard scalar diagnostics
   - OMB histogram (QC2 == 0)
   - Optional OMA overlay (if available)

2. GNSSRO fallback mode
   - If OMB is missing, the histogram is generated from ObsValue only.

QC2 filtering is applied consistently, and all arrays are flattened
before histogramming.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from .utils_loaders import (
    load_qc_any,
    load_obsvalue,
    load_omb,
    load_oma_explicit,
)


def plot_scalar_hist(f, varname, label, outdir):
    """
    Plot histogram diagnostics for scalar observations.

    This function supports two workflows:

    1. **GNSSRO fallback mode**

       If OMB is missing, the function plots a histogram of ``ObsValue`` only.
       This matches the behavior of legacy GNSSRO diagnostics.

    2. **Standard scalar mode**

       If OMB exists, the function plots:

       - OMB histogram (QC2 == 0)
       - Optional OMA overlay (if available)

    Parameters
    ----------
    f : xarray.Dataset or dict-like
        Observation diagnostics file containing QC, ObsValue, OMB, OMA.
    varname : str
        Name of the scalar variable (e.g., ``"air_temperature"``).
    label : str
        Short label used in plot titles and output filenames.
    outdir : str
        Directory where output PNG files will be written.

    Notes
    -----
    - QC2 filtering is applied using ``load_qc_any``.
    - All arrays are flattened before histogramming.
    - KDE is not used here (unlike unified histograms) to preserve
      legacy behavior.
    - One PNG file is produced per variable.

    Returns
    -------
    None
        A PNG file is written to ``outdir``.
    """
    os.makedirs(outdir, exist_ok=True)

    qc2 = load_qc_any(f, varname)
    if qc2 is None:
        print(f"[SKIP] {label} scalar hist: QC missing")
        return

    obs = load_obsvalue(f, varname)
    if obs is None:
        print(f"[SKIP] {label} scalar hist: ObsValue missing")
        return

    # Flatten everything
    qc2 = qc2.ravel()
    obs = obs.ravel()

    # Try to load OMB/OMA
    omb = load_omb(f, varname)
    oma = load_oma_explicit(f, varname)

    # ------------------------------------------------------------
    # GNSSRO fallback: no OMB → plot ObsValue only
    # ------------------------------------------------------------
    if omb is None:
        print(f"[INFO] {label}: No OMB found — using ObsValue only")

        valid = (qc2 == 0) & np.isfinite(obs)
        if np.sum(valid) == 0:
            print(f"[SKIP] {label}: no valid ObsValue")
            return

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(obs[valid], bins=120, color="lightgrey", edgecolor=None, alpha=0.7)
        ax.set_title(f"{label} ObsValue Histogram (QC2==0)")
        ax.set_xlabel("ObsValue")
        ax.set_ylabel("Count")
        ax.grid(True, alpha=0.3)

        fname = os.path.join(outdir, f"{label.lower()}_obsvalue_hist.png")
        fig.savefig(fname, dpi=150)
        plt.close(fig)
        print(f"[SAVED] {fname}")
        return

    # ------------------------------------------------------------
    # Normal scalar OMB/OMA histogram (for conventional obs)
    # ------------------------------------------------------------
    omb = omb.ravel()
    if oma is not None:
        oma = oma.ravel()

    valid_omb = (qc2 == 0) & np.isfinite(omb)

    if np.sum(valid_omb) == 0:
        print(f"[SKIP] {label}: no valid OMB")
        return

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(omb[valid_omb], bins=120, color="lightgrey", edgecolor=None, alpha=0.7)
    ax.set_title(f"{label} OMB Histogram (QC2==0)")
    ax.set_xlabel("OMB")
    ax.set_ylabel("Count")
    ax.grid(True, alpha=0.3)

    fname = os.path.join(outdir, f"{label.lower()}_omb_hist.png")
    fig.savefig(fname, dpi=150)
    plt.close(fig)
    print(f"[SAVED] {fname}")
