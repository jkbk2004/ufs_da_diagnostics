
UFS-DA Diagnostics
==================

The **UFS-DA Diagnostics Toolkit** provides a unified, modular set of tools for
visualizing and analyzing FV3-JEDI data assimilation diagnostics. It supports:

- Spectral diagnostics (tile-based and background/increment comparisons)
- Increment map diagnostics (single experiment and CTRL–EXP–DIFF)
- Observation-space diagnostics
- JEDI log parsing and summary extraction
- YAML-driven configuration
- Command-line tools for streamlined workflows

The package is organized into four major subsystems:

- ``spectra`` — spectral energy diagnostics on FV3 cubed-sphere tiles
- ``increment`` — horizontal increment maps and zonal-mean diagnostics
- ``obs`` — observation-space diagnostics and QC visualization
- ``log`` — FV3-JEDI log parsing utilities

All diagnostics can be run from the command line using the provided entry points.

Quick Start
-----------

Install the package in editable mode:

.. code-block:: bash

    pip install -e .

Run a diagnostic using a YAML configuration:

.. code-block:: bash

    ufsda-inc-maps --yaml diag_fv3-jedi-tiles.yaml

Available CLI Tools
-------------------

The toolkit provides several command-line utilities:

- ``ufsda-spectra-ctl-exp`` — Spectra diagnostics for CTRL/EXP tile-based fields
- ``ufsda-spectra-bkg-inc`` — Background vs increment spectral comparison
- ``ufsda-inc-maps`` — Increment maps and zonal-mean diagnostics
- ``ufsda-obs-diag`` — Observation-space diagnostics
- ``ufsda-jedi-log`` — Parse and summarize FV3-JEDI logs

Documentation Structure
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   usage_spectra
   usage_increment
   usage_obs
   usage_logs

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/spectra
   api/increment
   api/obs
   api/plots
   api/log

.. toctree::
   :maxdepth: 1
   :caption: Developer Guide

   developer_guide

Project Goals
-------------

The goal of this project is to provide a unified, extensible diagnostics
framework for UFS-DA workflows, enabling:

- Consistent visualization across experiments
- Reproducible YAML-driven workflows
- Modular Python APIs for advanced users
- HPC-friendly batch diagnostics
- Extensibility for new diagnostics and research workflows
