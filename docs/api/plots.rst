Plotting Subsystem API
======================

The plotting subsystem provides all figure‑generation utilities used by
the diagnostics drivers. This includes ATMS observation plots, scalar
and vector histograms, QC summaries, spectra visualizations, and shared
plotting utilities.

This page documents the full plotting engine under
``ufs_da_diagnostics.plots``.


Modules
-------

.. automodule:: ufs_da_diagnostics.plots.base_plotter
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: ufs_da_diagnostics.plots.obs_diag_plotter
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.spectra_plots
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.scalar_hist
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.vector_hist
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.atms_hist
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.atms_latbins
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.atms_scan_position
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.atms_stats
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.atms_stats_extended
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.qc_plots
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.utils
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.utils_common
    :members:
    :undoc-members:

.. automodule:: ufs_da_diagnostics.plots.utils_loaders
    :members:
    :undoc-members:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.plots.base_plotter.BasePlotter

    ufs_da_diagnostics.plots.obs_diag_plotter.ObsDiagPlotter
    ufs_da_diagnostics.plots.obs_diag_plotter.plot_atms_histograms
    ufs_da_diagnostics.plots.obs_diag_plotter.plot_scalar_histograms
    ufs_da_diagnostics.plots.obs_diag_plotter.plot_vector_histograms

    ufs_da_diagnostics.plots.spectra_plots.SpectraPlotter
    ufs_da_diagnostics.plots.spectra_plots.plot_spectra_1d
    ufs_da_diagnostics.plots.spectra_plots.plot_spectra_2d

    ufs_da_diagnostics.plots.scalar_hist.plot_scalar_hist
    ufs_da_diagnostics.plots.vector_hist.plot_vector_hist

    ufs_da_diagnostics.plots.atms_hist.plot_atms_hist
    ufs_da_diagnostics.plots.atms_latbins.plot_atms_latbins
    ufs_da_diagnostics.plots.atms_scan_position.plot_atms_scanpos
    ufs_da_diagnostics.plots.atms_stats.plot_atms_stats
    ufs_da_diagnostics.plots.atms_stats_extended.plot_atms_stats_extended

    ufs_da_diagnostics.plots.qc_plots.plot_qc_summary

    ufs_da_diagnostics.plots.utils.load_variable
    ufs_da_diagnostics.plots.utils_common.apply_style
    ufs_da_diagnostics.plots.utils_loaders.load_ioda_variable


Detailed API
------------

BasePlotter
~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.plots.base_plotter.BasePlotter
    :members:
    :undoc-members:
    :show-inheritance:


ObsDiagPlotter
~~~~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.plots.obs_diag_plotter.ObsDiagPlotter
    :members:
    :undoc-members:


SpectraPlotter
~~~~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.plots.spectra_plots.SpectraPlotter
    :members:
    :undoc-members:


ATMS Plot Modules
~~~~~~~~~~~~~~~~~

.. automodule:: ufs_da_diagnostics.plots.atms_hist
    :members:

.. automodule:: ufs_da_diagnostics.plots.atms_latbins
    :members:

.. automodule:: ufs_da_diagnostics.plots.atms_scan_position
    :members:

.. automodule:: ufs_da_diagnostics.plots.atms_stats
    :members:

.. automodule:: ufs_da_diagnostics.plots.atms_stats_extended
    :members:


Histogram Modules
~~~~~~~~~~~~~~~~~

.. automodule:: ufs_da_diagnostics.plots.scalar_hist
    :members:

.. automodule:: ufs_da_diagnostics.plots.vector_hist
    :members:


QC Plotting
~~~~~~~~~~~

.. automodule:: ufs_da_diagnostics.plots.qc_plots
    :members:


Shared Utilities
~~~~~~~~~~~~~~~~

.. automodule:: ufs_da_diagnostics.plots.utils
    :members:

.. automodule:: ufs_da_diagnostics.plots.utils_common
    :members:

.. automodule:: ufs_da_diagnostics.plots.utils_loaders
    :members:
