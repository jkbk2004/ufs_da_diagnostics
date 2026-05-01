"""
QC Diagnostics Plotting
=======================

This module provides a simple bar‑chart visualization of QC pass/fail
counts. It is used by various diagnostics workflows to summarize the
number of assimilated (QC==0) and rejected (QC!=0) observations.

The ``QCPlotter`` class inherits from ``BasePlotter`` to ensure
consistent styling and figure layout across the diagnostics suite.
"""

import matplotlib.pyplot as plt
from .base_plotter import BasePlotter


class QCPlotter(BasePlotter):
    """
    Plotter for QC pass/fail summary charts.

    This class extends ``BasePlotter`` and provides a single method,
    ``plot_qc_counts()``, which generates a bar chart showing the number
    of observations that passed QC filtering versus those that failed.

    Notes
    -----
    - This plot is intentionally simple and is typically used as a
      high‑level summary.
    - The figure uses the standardized styling defined in
      ``BasePlotter``.
    """

    def plot_qc_counts(self, qc_pass, qc_fail, fname=None):
        """
        Plot a bar chart of QC pass/fail counts.

        Parameters
        ----------
        qc_pass : int
            Number of observations with QC==0 (assimilated).
        qc_fail : int
            Number of observations with QC!=0 (rejected).
        fname : str, optional
            Output filename for saving the figure. If ``None``, the
            figure is not saved.

        Returns
        -------
        None
            The figure is displayed only if ``fname`` is not provided.
            When ``fname`` is given, the figure is saved and closed.

        Notes
        -----
        - Bars are colored green (pass) and red (fail).
        - The top‑level title is added using ``BasePlotter.add_title()``.
        """
        fig = self.new_figure(width=6, height=5)
        self.add_title(fig, "QC Pass/Fail Counts")

        labels = ["Pass", "Fail"]
        values = [qc_pass, qc_fail]

        plt.bar(labels, values, color=["seagreen", "firebrick"])
        plt.ylabel("Count")

        if fname:
            plt.savefig(fname, dpi=200)
        plt.close(fig)
