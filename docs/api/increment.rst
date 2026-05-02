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
    :noindex:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    load_tile
    load_grid
    load_pressure
    build_global
    compute_zonal_mean_full


Detailed API
------------

Tile Loading
~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_tile
   :no-index:

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_grid
   :no-index:

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.load_pressure
   :no-index:

Global Field Construction
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.build_global
   :no-index:

Zonal Mean Diagnostics
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.increment.increment_maps_tiles.compute_zonal_mean_full
   :no-index:
