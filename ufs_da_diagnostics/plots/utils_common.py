#!/usr/bin/env python3
"""
Common Plotting Utilities for FV3-JEDI Observation Diagnostics
==============================================================

This module provides shared helper functions used across the plotting
subsystem, including:

- Filesystem helpers
- Assimilated-count annotations
- ATMS channel-group shading and legends
- Safe KDE plotting
- Channel tick formatting

These utilities ensure consistent styling and behavior across ATMS,
scalar, vector, and spectra diagnostics.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches


# ----------------------------------------------------------------------
# Filesystem helpers
# ----------------------------------------------------------------------

def make_output_dir(path):
    """
    Create an output directory if it does not already exist.

    Parameters
    ----------
    path : str
        Directory path to create.

    Returns
    -------
    str
        The same directory path, for convenience.

    Notes
    -----
    - ``exist_ok=True`` ensures the function is safe to call repeatedly.
    """
    os.makedirs(path, exist_ok=True)
    return path


# ----------------------------------------------------------------------
# Annotation helpers
# ----------------------------------------------------------------------

def annotate_assimilated(fig, N):
    """
    Add a small annotation showing the number of assimilated observations.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure on which to place the annotation.
    N : int
        Number of assimilated observations (QC==0).

    Notes
    -----
    - The annotation is placed in the lower-right corner of the figure.
    - Used by ATMS and scalar histogram diagnostics.
    """
    txt = f"N assimilated: {N}"
    fig.text(0.99, 0.01, txt,
             ha="right", va="bottom",
             fontsize=9, color="dimgray")


# ----------------------------------------------------------------------
# ATMS shading helpers
# ----------------------------------------------------------------------

def shade_atms(ax):
    """
    Apply ATMS channel-group shading to an axis.

    The shading follows NOAA's standard ATMS grouping:

    - Window channels: 1–2 and 16–17
    - O₂ Temperature channels: 3–15
    - H₂O channels: 18–22

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis on which to apply shading.

    Notes
    -----
    - Assumes the x-axis corresponds to 1-based channel numbers.
    - Used by ATMS mean/std plots and extended diagnostics.
    """
    # Window channels: 1–2 and 16–17
    ax.axvspan(0.5, 2.5,   color="#b0b0b0", alpha=0.45)   # Ch 1–2
    ax.axvspan(15.5, 17.5, color="#b0b0b0", alpha=0.45)   # Ch 16–17

    # O2 temperature channels: 3–15
    ax.axvspan(2.5, 15.5,  color="#7fb3ff", alpha=0.35)

    # Water vapor channels: 18–22
    ax.axvspan(17.5, 22.5, color="#7fdc7f", alpha=0.35)


def atms_group_legend(ax, loc="lower right", fontsize=9):
    """
    Add an ATMS channel-group legend to an axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to which the legend will be added.
    loc : str, optional
        Legend location (default ``"lower right"``).
    fontsize : int, optional
        Legend font size.

    Notes
    -----
    - Colors match those used in ``shade_atms``.
    - Used by ATMS stats and extended stats plots.
    """
    patch_window = mpatches.Patch(color="#b0b0b0", alpha=0.45, label="Window")
    patch_o2     = mpatches.Patch(color="#7fb3ff", alpha=0.35, label="O₂ Temp")
    patch_h2o    = mpatches.Patch(color="#7fdc7f", alpha=0.35, label="H₂O")

    ax.legend(handles=[patch_window, patch_o2, patch_h2o],
              loc=loc, fontsize=fontsize, frameon=True)


# ----------------------------------------------------------------------
# KDE helper
# ----------------------------------------------------------------------

def kde_safe(ax, data, color="dimgray", linewidth=2, label=None):
    """
    Safely draw a KDE curve if the data is valid and non-degenerate.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis on which to draw the KDE.
    data : array-like
        Input data array.
    color : str, optional
        Line color (default ``"dimgray"``).
    linewidth : float, optional
        Line width (default 2).
    label : str, optional
        Legend label.

    Notes
    -----
    - KDE is skipped if:
      - fewer than 10 valid points exist
      - the data has zero variance
      - seaborn raises an exception
    - Used by unified histograms and ATMS histograms.
    """
    data = np.asarray(data)
    data = data[np.isfinite(data)]
    if data.size < 10:
        return
    if np.allclose(np.std(data), 0.0):
        return
    try:
        sns.kdeplot(data, color=color, linewidth=linewidth, ax=ax, label=label)
    except Exception:
        pass


# ----------------------------------------------------------------------
# Axis helpers
# ----------------------------------------------------------------------

def clean_channel_ticks(ax, nchans):
    """
    Set clean, readable x-axis ticks for channel-based plots.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to modify.
    nchans : int
        Number of channels.

    Notes
    -----
    - For ≤22 channels, every channel is labeled.
    - For >22 channels, ticks are spaced every 2 channels.
    - Used by ATMS stats and extended stats plots.
    """
    ax.set_xlim(0.5, nchans + 0.5)
    if nchans <= 22:
        ax.set_xticks(np.arange(1, nchans + 1, 1))
    else:
        ax.set_xticks(np.arange(1, nchans + 1, 2))
    ax.set_xlabel("Channel")
