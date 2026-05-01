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

Subsystem Relationships
-----------------------

The diagram below shows how the diagnostics subsystems relate to each
other within ``ufs-da-diagnostics``:

.. mermaid::

    graph TD

        A[Observation Diagnostics<br/>(YAML-driven)] --> B[ObsDiagPlotter<br/>plots.obs_diag_plotter]
        A --> C[Observation Utilities<br/>obs.utils]

        D[Increment Diagnostics<br/>(tile maps, zonal means)] --> E[Increment Maps Tiles<br/>increment.increment_maps_tiles]
        D --> F[Increment Core<br/>increment.increment_core]

        G[Spectral Diagnostics] --> H[SpectraPlotter<br/>plots.spectra_plots]
        G --> I[Spectral Core<br/>spectra.spectra_core]

        B --> J[Plotting Subsystem<br/>plots.utils]
        E --> J
        H --> J

        K[JEDI Log Tools] --> L[LogParser<br/>logs.log_parser]

        C --> M[IODA Files]
        E --> N[FV3 Increment Files]
        H --> N

        style A fill:#d9e8ff,stroke:#4a78c2,stroke-width:1px
        style D fill:#d9e8ff,stroke:#4a78c2,stroke-width:1px
        style G fill:#d9e8ff,stroke:#4a78c2,stroke-width:1px
        style K fill:#d9e8ff,stroke:#4a78c2,stroke-width:1px

        style B fill:#e8f5e9,stroke:#2e7d32
        style C fill:#e8f5e9,stroke:#2e7d32
        style E fill:#e8f5e9,stroke:#2e7d32
        style F fill:#e8f5e9,stroke:#2e7d32
        style H fill:#e8f5e9,stroke:#2e7d32
        style I fill:#e8f5e9,stroke:#2e7d32
        style L fill:#e8f5e9,stroke:#2e7d32
        style J fill:#fff3cd,stroke:#b8860b

