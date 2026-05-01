Observation Tools Overview
==========================

The ``ufs-da-diagnostics`` package provides two categories of
observation‑related tools:

1. **Observation Diagnostics**  
   YAML‑driven plotting for ATMS, scalar, and vector observations.

2. **Observation Inspection Utilities**  
   Python helpers for exploring IODA files (variables, groups, metadata).

This page provides a high‑level overview and links to the detailed usage
pages.


Observation Diagnostics
-----------------------

These tools generate:

- Histograms (OMB/OMA)
- ATMS channel statistics
- Scan‑position diagnostics
- Latitude‑binned diagnostics
- Vector U/V histograms

See :doc:`usage_observation_tools` for full details.


Observation Inspection
----------------------

These utilities help users explore IODA files:

- List variables  
- List groups  
- Inspect metadata  

Useful when preparing YAML configurations for diagnostics.

See :doc:`usage_observation_tools` for examples.


JEDI Log Tools
--------------

Tools for parsing FV3‑JEDI logs:

- Iteration summaries  
- Cost‑function components  
- QC summaries  
- Timing information  

See :doc:`usage_logs` for details.
