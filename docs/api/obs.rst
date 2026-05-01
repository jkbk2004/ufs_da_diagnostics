Observation Diagnostics API
===========================

The observation diagnostics subsystem provides tools for generating
statistics, histograms, scan‑position plots, and latitudinal bin
summaries from IODA observation files. These diagnostics are used
by the CLI driver ``ufsda-obs-diagnostic`` and by the plotting
subsystem under ``ufs_da_diagnostics.plots``.

This page documents the core observation diagnostics engine.


Modules
-------

.. automodule:: ufs_da_diagnostics.obs.obs_diagnostic
    :members:
    :undoc-members:
    :show-inheritance:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.obs.obs_diagnostic.ObsDiagnostic
    ufs_da_diagnostics.obs.obs_diagnostic.load_ioda
    ufs_da_diagnostics.obs.obs_diagnostic.compute_statistics
    ufs_da_diagnostics.obs.obs_diagnostic.run_diagnostics


Detailed API
------------

ObsDiagnostic
~~~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.obs.obs_diagnostic.ObsDiagnostic
    :members:
    :undoc-members:
    :show-inheritance:


Module‑Level Functions
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.load_ioda

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.compute_statistics

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.run_diagnostics

