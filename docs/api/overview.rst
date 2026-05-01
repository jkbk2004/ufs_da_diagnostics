Diagnostics API Overview
========================

The ``ufs_da_diagnostics`` package provides a modular, extensible
framework for generating diagnostics from FV3-JEDI experiments. The
toolkit is organized into four primary subsystems:

- **Spectra** — compute wavenumber spectra and spectral ratios
- **Increment Maps** — generate tile maps, global stitched maps, and zonal means
- **Observation Diagnostics** — compute statistics and summaries from IODA files
- **Logs** — parse JEDI variational DA logs into structured diagnostics

This page provides a high-level architectural overview of the full
diagnostics engine and links to the detailed API pages for each
subsystem.


Architecture
------------

The diagnostics package is structured as a set of modular subsystems,
each with its own API, CLI entry points, and plotting utilities.

```mermaid
flowchart TD

    A[CLI Drivers] --> B[Spectra Subsystem]
    A --> C[Increment Subsystem]
    A --> D[Observation Subsystem]
    A --> E[Log Subsystem]

    B --> B1[SpectraCore]
    B --> B2[Spectra Analysis Drivers]
    B --> B3[Spectra Plotting]

    C --> C1[IncrementMaps]
    C --> C2[Tile Maps / Global Maps]
    C --> C3[Zonal Means]

    D --> D1[ObsDiagnostic]
    D --> D2[IODA Loaders]
    D --> D3[Obs Plotting]

    E --> E1[Log Parser]
    E --> E2[Cost Function Diagnostics]
    E --> E3[Jo / Departures / Obs Errors]
