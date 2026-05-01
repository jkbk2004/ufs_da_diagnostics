"""
Base Plotter Utilities
======================

This module defines ``BasePlotter``, a lightweight helper class that
standardizes figure creation and title placement across all diagnostics
plots in the ``ufs_da_diagnostics`` package.

It provides:

- Consistent Matplotlib styling (fonts, tick sizes, legend sizes)
- A unified ``new_figure()`` method with controlled margins
- A robust ``add_title()`` method using a dedicated title axis

All higher‑level plotters (increment maps, spectra, obs diagnostics,
ATMS diagnostics, QC plots, etc.) inherit or use this class to ensure
visual consistency across the entire diagnostics suite.
"""

import matplotlib.pyplot as plt


class BasePlotter:
    """
    Base class providing consistent figure styling and layout helpers.

    This class configures global Matplotlib parameters for uniform
    appearance across all diagnostics plots. It also provides helper
    methods for creating figures with standardized margins and adding
    top‑level titles using a dedicated axis.

    Notes
    -----
    - ``plt.rcParams`` is updated at initialization to ensure consistent
      font sizes and label formatting.
    - ``new_figure()`` returns a figure with controlled margins suitable
      for multi‑panel layouts.
    - ``add_title()`` places a title in a fixed top region using an
      invisible axis, ensuring stable spacing regardless of subplot
      configuration.
    """

    def __init__(self):
        """Initialize global Matplotlib style parameters."""
        plt.rcParams.update({
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10
        })

    def new_figure(self, width=18, height=6, top=0.90):
        """
        Create a new figure with standardized margins.

        Parameters
        ----------
        width : float, optional
            Figure width in inches (default 18).
        height : float, optional
            Figure height in inches (default 6).
        top : float, optional
            Top margin for subplot area (default 0.90).

        Returns
        -------
        matplotlib.figure.Figure
            A new figure with predefined margins and spacing.

        Notes
        -----
        - ``wspace`` is set to 0.25 for multi‑panel horizontal spacing.
        - ``left``/``right``/``bottom`` margins are tuned for diagnostics.
        """
        fig = plt.figure(figsize=(width, height))
        fig.subplots_adjust(left=0.05, right=0.98, top=top, bottom=0.12, wspace=0.25)
        return fig

    def add_title(self, fig, text):
        """
        Add a top‑level title using a dedicated invisible axis.

        Parameters
        ----------
        fig : matplotlib.figure.Figure
            Figure to which the title will be added.
        text : str
            Title text.

        Notes
        -----
        - A dedicated axis is added above the subplot grid.
        - This avoids layout conflicts with ``suptitle()`` and ensures
          consistent vertical spacing across all diagnostics figures.
        """
        title_ax = fig.add_axes([0.01, 0.91, 0.98, 0.045])
        title_ax.text(0, 0.5, text, fontsize=16, ha='left', va='center')
        title_ax.set_axis_off()
