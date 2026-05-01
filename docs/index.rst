UFS-DA Diagnostics
==================

The **UFS-DA Diagnostics Toolkit** provides modular, YAML-driven tools for
visualizing and analyzing FV3-JEDI data assimilation diagnostics. It includes:

- Spectral diagnostics (tile-based and background/increment)
- Increment maps and zonal-mean diagnostics
- Observation-space diagnostics (ATMS, scalar, vector)
- Observation inspection utilities
- JEDI log parsing
- Command-line tools for batch workflows

Use the navigation on the left to explore the User Guide and API Reference.

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart

   usage_spectra
   usage_increment

   usage_observation_overview
   usage_observation_tools
   usage_logs
   usage_plots


.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/overview
   api/spectra
   api/increment
   api/plots
   api/obs_diagnostic
   api/obs
   api/log


.. toctree::
   :maxdepth: 1
   :caption: Developer Guide

   developer_guide

Example YAML Files
------------------

The package includes ready-to-run example YAML configurations under:

``ufs_da_diagnostics/examples/``

These templates demonstrate the expected structure for each diagnostics subsystem:

- ``diag_fv3-jedi-bkg_inc.yaml`` — Background–increment spectral diagnostics
- ``diag_fv3-jedi_obs.yaml`` — Observation-space diagnostics
- ``diag_fv3-jedi-tiles.yaml`` — Increment maps and zonal-mean diagnostics

You can copy and modify these files to create your own diagnostic workflows.


