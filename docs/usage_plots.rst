Using Plotting Tools
====================

The plotting subsystem is used automatically by all CLI tools, but can
also be used directly.

Example: Plot a Scalar Histogram
--------------------------------

.. code-block:: python

    from ufs_da_diagnostics.plots.scalar_hist import plot_scalar_hist
    plot_scalar_hist(data, variable="t")


Example: Plot Spectra
---------------------

.. code-block:: python

    from ufs_da_diagnostics.plots.spectra_plots import plot_spectra_1d
    plot_spectra_1d(k, E)
