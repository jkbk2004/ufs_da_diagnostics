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

This page provides a high‑level overview of each subsystem, diagrams
showing how they relate, and links to the detailed API documentation.


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


Data Flow Overview
------------------

The following diagram shows how data moves through the diagnostics
framework:

.. mermaid::

    flowchart LR

        A[IODA Diagnostics Files] --> B[ObsDiagPlotter]
        B --> C[Plots (ATMS, Scalar, Vector)]

        D[FV3 Increment Files] --> E[Increment Maps Tiles]
        E --> F[Tile Maps & Zonal Means]

        D --> G[Spectra Core]
        G --> H[SpectraPlotter]
        H --> I[1D/2D Spectra]

        J[JEDI Log File] --> K[LogParser]
        K --> L[QC Summary, Iteration Summary, Timing]

        style B fill:#e8f5e9,stroke:#2e7d32
        style E fill:#e8f5e9,stroke:#2e7d32
        style H fill:#e8f5e9,stroke:#2e7d32
        style K fill:#e8f5e9,stroke:#2e7d32


Observation Diagnostics Driver Sequence
---------------------------------------

This sequence diagram shows how the YAML‑driven observation diagnostics
driver orchestrates the workflow:

.. mermaid::

    sequenceDiagram
        participant U as User
        participant D as obs_diagnostic
        participant P as ObsDiagPlotter
        participant F as File Loader
        participant G as Plotting Utils

        U->>D: python -m obs_diagnostic --yaml config.yaml
        D->>D: Parse YAML
        D->>P: Initialize plotter
        P->>F: Load IODA file
        F-->>P: Return variables, metadata
        P->>G: Generate plots (hist, stats, scanpos, latbins)
        G-->>P: Save figures
        P-->>D: Diagnostics complete
        D-->>U: Output written to <outdir>


Subsystem Summaries
-------------------

Observation Diagnostics
^^^^^^^^^^^^^^^^^^^^^^^

YAML‑driven diagnostics for:

- ATMS
- Scalar observations
- Vector observations

API Reference:

- :doc:`obs_diagnostic`
- :doc:`obs`
- :doc:`plots`

Usage:

- :doc:`../usage_observation_tools`


Increment Diagnostics
^^^^^^^^^^^^^^^^^^^^^

Tile‑based increment maps and zonal‑mean diagnostics.

API Reference:

- :doc:`increment`
- :doc:`plots`

Usage:

- :doc:`../usage_increment`


Spectral Diagnostics
^^^^^^^^^^^^^^^^^^^^

1D and 2D spectra for increment and background fields.

API Reference:

- :doc:`spectra`
- :doc:`plots`

Usage:

- :doc:`../usage_spectra`


Log Parsing Tools
^^^^^^^^^^^^^^^^^^

Extract iteration summaries, QC statistics, and timing from JEDI logs.

API Reference:

- :doc:`log`

Usage:

- :doc:`../usage_logs`


Observation Inspection Utilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List variables, groups, and metadata in IODA files.

API Reference:

- :doc:`obs`

Usage:

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
