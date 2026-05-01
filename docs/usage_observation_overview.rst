Observation Diagnostics Overview
================================

The observation diagnostics subsystem processes IODA files and generates
statistics, histograms, QC summaries, and ATMS-specific diagnostics.

Subsystem Components
--------------------

- ``ObsDiagnostic`` — core engine
- IODA loaders
- scalar and vector histograms
- ATMS diagnostics
- QC summaries
- plotting utilities


Workflow
--------

1. Load IODA file
2. Compute statistics
3. Generate plots
4. Save outputs
