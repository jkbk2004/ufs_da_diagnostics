Quickstart
==========

This quickstart demonstrates how to run the diagnostics toolkit using
the provided CLI tools and YAML configuration files.

Spectra Diagnostics
-------------------

Compute spectra comparing analysis increments between CTRL and EXP:

.. code-block:: bash

    ufsda-spectra-ana-inc --yaml spectra_ana_inc.yaml

Compute spectra comparing background vs increment:

.. code-block:: bash

    ufsda-spectra-bkg-inc --yaml spectra_bkg_inc.yaml


Increment Maps
--------------

Generate tile maps, global maps, and zonal means:

.. code-block:: bash

    ufsda-inc-maps --yaml increment_maps.yaml


Observation Diagnostics
-----------------------

Run observation diagnostics on an IODA file:

.. code-block:: bash

    ufsda-obs-diag --yaml obs_diag.yaml


Log Diagnostics
---------------

Parse a JEDI variational DA log:

.. code-block:: bash

    ufsda-jedi-log path/to/OUTPUT.fv3jedi --output report.txt


Running on Hercules
-------------------

The diagnostics toolkit is installed on the Hercules system at:

.. code-block:: bash

    /work/noaa/epic/jongkim/ufs_da_diagnostics

To use the preconfigured environment, source the Hercules Anaconda setup:

.. code-block:: bash

    source /work/noaa/epic/jongkim/hercules.anaconda

After sourcing the environment, all CLI tools (ufsda-spectra-ana-inc,
ufsda-spectra-bkg-inc, ufsda-inc-maps, ufsda-obs-diag, ufsda-jedi-log)
are available in the PATH and can be run directly from any directory.
