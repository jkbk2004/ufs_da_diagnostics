Plotting API
============

This section documents the plotting subsystem used throughout
``ufs-da-diagnostics``. It includes:

- Observation diagnostics plotting (ATMS, scalar, vector)
- Spectral diagnostics (1D/2D spectra)
- Shared plotting utilities

These modules are used internally by the YAML‑driven diagnostics driver
and can also be imported directly for custom workflows.


Observation Diagnostics Plotter
-------------------------------

The ``ObsDiagPlotter`` class orchestrates all observation‑space
diagnostics, including histograms, statistics, scan‑position diagnostics,
and latitude‑binned plots.

.. automodule:: ufs_da_diagnostics.plots.obs_diag_plotter
   :members:
   :undoc-members:
   :show-inheritance:


Spectral Diagnostics
--------------------

The ``SpectraPlotter`` class provides tools for computing and plotting
spectra from FV3‑JEDI increment and background fields.

.. automodule:: ufs_da_diagnostics.plots.spectra_plots
   :members:
   :undoc-members:
   :show-inheritance:


Shared Plot Utilities
---------------------

Common helper functions used across the plotting subsystem.

.. automodule:: ufs_da_diagnostics.plots.utils
   :members:
   :undoc-members:
   :show-inheritance:


Related Usage Pages
-------------------

- :doc:`../usage_observation_tools` — Observation diagnostics workflow  
- :doc:`../usage_spectra` — Spectral diagnostics workflow  
- :doc:`../usage_increment` — Increment maps and zonal means  
