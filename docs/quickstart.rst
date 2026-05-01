Quickstart
==========

This quickstart demonstrates how to run the diagnostics toolkit using
the provided CLI tools and YAML configuration files.

Spectra Diagnostics
-------------------

Compute spectra comparing analysis increments between CTRL and EXP:

.. code-block:: bash

    ufsda-spectra-ana-inc config/spectra_ana_inc.yaml

Compute spectra comparing background vs increment:

.. code-block:: bash

    ufsda-spectra-bkg-inc config/spectra_bkg_inc.yaml


Increment Maps
--------------

Generate tile maps, global maps, and zonal means:

.. code-block:: bash

    ufsda-increment-maps config/increment_maps.yaml


Observation Diagnostics
-----------------------

Run observation diagnostics on an IODA file:

.. code-block:: bash

    ufsda-obs-diagnostic config/obs_diag.yaml


Log Diagnostics
---------------

Parse a JEDI variational DA log:

.. code-block:: bash

    ufsda-log-diagnostic config/log_diag.yaml


Minimal YAML Example
--------------------

.. code-block:: yaml

    experiment:
      name: EXP
      increment_file: inc.nc4
      background_file: bkg.nc4

    output:
      directory: diagnostics/
      plots: true
      save_data: true

    variables:
      - u
      - v
      - t
      - ps
