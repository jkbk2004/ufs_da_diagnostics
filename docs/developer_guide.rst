Developer Guide
===============

This guide provides an overview of the internal architecture of
``ufs-da-diagnostics`` and describes how to extend or modify the
diagnostics framework. It is intended for developers contributing new
diagnostics, adding plotting capabilities, or integrating additional
FV3‑JEDI data products.

The diagnostics system is modular and organized into subsystems:

- Observation diagnostics (YAML-driven)
- Increment diagnostics (tile maps, zonal means)
- Spectral diagnostics (1D/2D spectra)
- Plotting subsystem (shared utilities)
- Log parsing tools
- Observation inspection utilities


Project Structure
-----------------

The top-level package layout is:

.. code-block:: text

    ufs_da_diagnostics/
      increment/
        increment_maps_tiles.py
        increment_core.py
      obs/
        obs_diagnostic.py
        utils.py
      plots/
        obs_diag_plotter.py
        spectra_plots.py
        utils.py
      spectra/
        spectra_core.py
      logs/
        log_parser.py

      __init__.py
      version.py


Design Principles
-----------------

The diagnostics framework follows several core principles:

- **Modularity**  
  Each subsystem (obs, increment, spectra, logs) is independent.

- **YAML-driven workflows**  
  High-level drivers read YAML configs and orchestrate diagnostics.

- **Thin drivers, thick modules**  
  Drivers only parse YAML and call plotters; logic lives in modules.

- **Unified plotting subsystem**  
  All figures use shared utilities for consistency.

- **Extensibility**  
  New diagnostics can be added without modifying existing ones.


Adding New Observation Diagnostics
----------------------------------

Observation diagnostics are orchestrated by ``ObsDiagPlotter`` and
configured through YAML. To add a new diagnostic:

1. Add a new method to ``plots/obs_diag_plotter.py``  
   Example:

   .. code-block:: python

       def plot_new_metric(self, data, outdir):
           # compute metric
           # generate figure
           # save output

2. Add YAML support in ``obs_diagnostic.py``  
   Example:

   .. code-block:: python

       if diag_cfg.get("new_metric", False):
           plotter.plot_new_metric(data, outdir)

3. Document the new diagnostic in:

   - ``usage_observation_tools.rst``
   - ``api/plots.rst``


Adding New Increment Diagnostics
--------------------------------

Increment diagnostics are handled by:

- ``increment_maps_tiles.py`` (plotting)
- ``increment_core.py`` (data extraction)

To add a new increment diagnostic:

1. Add a computation routine to ``increment_core.py``  
2. Add a plotting routine to ``increment_maps_tiles.py``  
3. Update ``usage_increment.rst``  
4. Add API documentation in ``api/increment.rst``


Adding New Spectral Diagnostics
-------------------------------

Spectral diagnostics use:

- ``spectra_core.py`` for FFT and binning
- ``spectra_plots.py`` for visualization

To extend spectral diagnostics:

1. Add a new computation function to ``spectra_core.py``  
2. Add a new plotting method to ``spectra_plots.py``  
3. Update ``usage_spectra.rst``  
4. Update ``api/spectra.rst``


Plotting Subsystem
------------------

All diagnostics rely on shared utilities in ``plots/utils.py``:

- Color maps
- Figure layout helpers
- Shared annotation functions
- File naming conventions

When adding new plots:

- Reuse existing utilities whenever possible
- Add new utilities only if they are general-purpose


Coding Standards
----------------

The project follows:

- **PEP8** for formatting  
- **Google-style docstrings**  
- **Sphinx autodoc/autosummary** for API documentation  
- **YAML schemas** for configuration files  

Docstring example:

.. code-block:: python

    def compute_metric(x, y):
        """Compute a diagnostic metric.

        Args:
            x (np.ndarray): Input field.
            y (np.ndarray): Comparison field.

        Returns:
            float: Computed metric.
        """
        ...


Testing
-------

Tests should be added under ``tests/`` and follow ``pytest`` conventions.

Recommended test types:

- Unit tests for core computation modules
- Smoke tests for plotters (ensure they run without error)
- YAML-driven integration tests


Documentation Workflow
----------------------

Documentation is built using Sphinx with:

- ``autodoc``  
- ``autosummary``  
- ``napoleon`` (Google-style docstrings)  
- ``mermaid`` diagrams  

To add documentation:

1. Add docstrings to the module  
2. Add an entry in the appropriate ``api/*.rst`` file  
3. Add examples in the corresponding ``usage_*.rst`` page  
4. Update ``index.rst`` if needed


Extending the Framework
-----------------------

To add a new diagnostics subsystem:

1. Create a new directory under ``ufs_da_diagnostics/``  
2. Add core computation modules  
3. Add plotting modules  
4. Add a YAML-driven driver (optional)  
5. Add usage documentation  
6. Add API documentation  
7. Add tests  
8. Update the architecture diagram in ``api/overview.rst``


Developer Resources
-------------------

- :doc:`api/overview` — Architecture and subsystem diagrams  
- :doc:`api/plots` — Plotting subsystem  
- :doc:`api/increment` — Increment diagnostics  
- :doc:`api/spectra` — Spectral diagnostics  
- :doc:`api/obs_diagnostic` — Observation diagnostics driver  
- :doc:`api/log` — Log parsing tools  
