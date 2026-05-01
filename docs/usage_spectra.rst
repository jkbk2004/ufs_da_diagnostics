Using Spectra Diagnostics
=========================

Analysis Increment Spectra
--------------------------

.. code-block:: bash

    ufsda-spectra-ana-inc config/spectra_ana_inc.yaml


Background vs Increment Spectra
-------------------------------

.. code-block:: bash

    ufsda-spectra-bkg-inc config/spectra_bkg_inc.yaml


YAML Example
------------

.. code-block:: yaml

    experiment:
      ctrl: CTRL
      exp: EXP
      ctrl_increment: ctrl_inc.nc4
      exp_increment: exp_inc.nc4

    output:
      directory: spectra/
      plots: true
