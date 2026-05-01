Diagnostics API Overview
========================

The ``ufs-da-diagnostics`` package provides a modular diagnostics
framework for FV3‑JEDI data assimilation workflows. The diagnostics
system is organized into several subsystems, each responsible for a
specific class of analysis:

- Observation diagnostics (ATMS, scalar, vector)
- Increment diagnostics (tile maps, zonal means)
- Spectral diagnostics (1D/2D spectra)
- Plotting subsystem (shared plotting utilities)
- Log parsing tools (FV3‑JEDI logs)
- Observation inspection utilities (IODA structure exploration)

This page provides a high‑level overview of each subsystem and links to
their detailed API documentation.


Observation Diagnostics
-----------------------

Observation‑space diagnostics are driven by a YAML configuration file
and executed through the ``obs_diagnostic`` driver. These diagnostics
produce histograms, statistics, scan‑position plots, and latitude‑binned
diagnostics for ATMS, scalar, and vector observations.

API Reference:

- :doc:`obs_diagnostic`
- :doc:`obs` (observation utilities)
- :doc:`plots` (observation plotting classes)

Related Usage:

- :doc:`../usage_observation_tools`


Increment Diagnostics
---------------------

Increment diagnostics generate tile‑based increment maps and zonal‑mean
plots from FV3‑JEDI increment files. These tools support single‑ and
dual‑experiment comparisons.

API Reference:

- :doc:`increment`
- :doc:`plots` (increment plotting utilities)

Related Usage:

- :doc:`../usage_increment`


Spectral Diagnostics
--------------------

Spectral diagnostics compute and visualize 1D and 2D spectra from
increment and background fields. These tools are used to analyze
scale‑dependent behavior and compare spectral characteristics between
experiments.

API Reference:

- :doc:`spectra`
- :doc:`plots` (spectral plotting utilities)

Related Usage:

- :doc:`../usage_spectra`


Plotting Subsystem
------------------

The plotting subsystem provides shared utilities used across all
diagnostics:

- Observation diagnostics plotting
- Spectral plotting
- Increment plotting
- Shared color maps, figure helpers, and layout utilities

API Reference:

- :doc:`plots`


Log Parsing Tools
-----------------

The log parsing subsystem extracts iteration summaries, QC statistics,
and timing information from FV3‑JEDI logs.

API Reference:

- :doc:`log`

Related Usage:

- :doc:`../usage_logs`


Observation Inspection Utilities
--------------------------------

Lightweight helpers for exploring IODA files:

- List variables
- List groups
- Inspect metadata

API Reference:

- :doc:`obs`

Related Usage:

- :doc:`../usage_observation_tools`


Summary
-------

The diagnostics framework is modular and extensible, allowing users to:

- Run diagnostics via YAML‑driven drivers
- Import plotting classes directly for custom workflows
- Inspect observation files
- Parse JEDI logs
- Combine diagnostics across subsystems

Use the links above to explore each subsystem in detail.
