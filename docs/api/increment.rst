Increment Maps API
==================

The increment maps subsystem provides tools for generating horizontal
FV3 6‑tile increment maps and zonal‑mean diagnostics from FV3‑JEDI
analysis increment files. It supports both single‑experiment and
two‑experiment (CTRL–EXP–DIFF) workflows and is fully YAML‑driven.

This API reference documents the public functions and internal helpers
implemented in:

``ufs_da_diagnostics.increment.increment_maps_tiles``

For usage examples and YAML configuration details, see:

- :doc:`../usage_increment`


Module Summary
--------------

.. autosummary::
   :toctree: generated/
   :nosignatures:

   ufs_da_diagnostics.increment.increment_maps_tiles.load_yaml_config
   ufs_da_diagnostics.increment.increment_maps_tiles.load_tile_increment
   ufs_da_diagnostics.increment.increment_maps_tiles.stitch_tiles_to_latlon
   ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean
   ufs_da_diagnostics.increment.increment_maps_tiles.plot_increment_map
   ufs_da_diagnostics.increment.increment_maps_tiles.plot_zonal_mean
   ufs_da_diagnostics.increment.increment_maps_tiles.main


Full Module Documentation
-------------------------

.. automodule:: ufs_da_diagnostics.increment.increment_maps_tiles
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:
