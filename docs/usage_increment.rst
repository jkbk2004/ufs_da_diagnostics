Using Increment Diagnostics
===========================

The increment diagnostics subsystem generates tile maps, global stitched
maps, and zonal mean summaries.

Running the CLI Tool
--------------------

.. code-block:: bash

    ufsda-increment-maps config/increment_maps.yaml


YAML Configuration
------------------

.. code-block:: yaml

    experiment:
      name: EXP
      increment_file: inc.nc4

    output:
      directory: increment_maps/
      plots: true

    variables:
      - u
      - v
      - t


Outputs
-------

- ``tile_maps/`` — 6-tile FV3 maps
- ``global_maps/`` — stitched global maps
- ``zonal_means/`` — zonal mean profiles
