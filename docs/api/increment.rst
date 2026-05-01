Increment Diagnostics API
=========================

This module provides tools for generating tile‑based increment maps and
zonal‑mean diagnostics from FV3‑JEDI increment files. These diagnostics
are used to visualize spatial increment structure and compare
experiment‑to‑experiment differences.

The increment plotting routines are used internally by the increment
driver and can also be imported directly for custom workflows.


Tile‑Based Increment Maps
-------------------------

The ``increment_maps_tiles`` module generates:

- Tile‑based increment maps for ``u``, ``v``, ``t``, ``ps`` and other variables
- Multi‑panel figures for single or dual‑experiment comparisons
- Optional zonal‑mean diagnostics
- Automatic handling of FV3 cubed‑sphere tile geometry

.. automodule:: ufs_da_diagnostics.increment.increment_maps_tiles
   :members:
   :undoc-members:
   :show-inheritance:


Increment Core Utilities
------------------------

Core helper functions used for reading increment files, extracting
variables, and preparing fields for plotting.

.. automodule:: ufs_da_diagnostics.increment.increment_core
   :members:
   :undoc-members:
   :show-inheritance:


Related Usage Pages
-------------------

- :doc:`../usage_increment` — Increment maps and zonal‑mean workflow  
- :doc:`../usage_spectra` — Spectral diagnostics  
- :doc:`../usage_observation_tools` — Observation diagnostics  
