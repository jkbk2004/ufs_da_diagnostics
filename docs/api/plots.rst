Plotting Subsystem API
======================

The plotting subsystem provides all figure-generation utilities used by
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
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.obs_diag_plotter
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.spectra_plots
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.scalar_hist
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.vector_hist
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.atms_hist
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.atms_latbins
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.atms_scan_position
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.atms_stats
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.atms_stats_extended
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.qc_plots
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.utils
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.utils_common
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.plots.utils_loaders
    :members:
    :undoc-members:
    :noindex:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    to_numeric_safe
    load_qc_universal
    load_obsvalue
    load_hofx
