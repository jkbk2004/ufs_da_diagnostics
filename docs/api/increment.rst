Increment Diagnostics API
=========================

The increment diagnostics subsystem provides tools for loading FV3-JEDI
increment tiles, constructing global stitched fields, and computing
zonal-mean cross sections.

This page documents the functions available in
``ufs_da_diagnostics.increment.increment_maps_tiles``.


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

    ufs_da_diagnostics.increment.increment_maps_tiles.load_tile
    ufs_da_diagnostics.increment.increment_maps_tiles.load_grid
    ufs_da_diagnostics.increment.increment_maps_tiles.load_pressure
    ufs_da_diagnostics.increment.increment_maps_tiles.build_global
    ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean_full


Detailed API
------------

Tile Loading
~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_tile

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_grid

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_pressure


Global Field Construction
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.build_global


Zonal Mean Diagnostics
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean_full

