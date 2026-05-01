Increment Diagnostics API
=========================

The increment diagnostics subsystem provides tools for generating
FV3-JEDI increment maps (per tile), global stitched maps, and zonal
mean summaries. These diagnostics are used by the CLI driver
``ufsda-increment-maps`` and form the core of the increment analysis
workflow.

This page documents the full increment‑mapping engine under
``ufs_da_diagnostics.increment``.


Modules
-------

.. automodule:: ufs_da_diagnostics.increment.increment_maps_tiles
    :members:
    :undoc-members:
    :show-inheritance:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.increment.increment_maps_tiles.IncrementMaps
    ufs_da_diagnostics.increment.increment_maps_tiles.load_increment
    ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean
    ufs_da_diagnostics.increment.increment_maps_tiles.plot_tile_map
    ufs_da_diagnostics.increment.increment_maps_tiles.plot_global_map


Detailed API
------------

IncrementMaps
~~~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.increment.increment_maps_tiles.IncrementMaps
    :members:
    :undoc-members:
    :show-inheritance:


Module‑Level Functions
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_increment

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.plot_tile_map

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.plot_global_map
