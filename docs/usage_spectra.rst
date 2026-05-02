Using Spectra Diagnostics
=========================

The spectra diagnostics compute the distribution of variance across
horizontal spatial scales for background fields, analysis increments,
and experiment‑to‑experiment differences. For the mathematical
formulation and example figures, see :ref:`Diagnostics Overview
<diagnostics_overview>`.

Two CLI drivers are provided:

- ``ufsda-spectra-ana-inc`` — compare analysis increments between CTRL and EXP  
- ``ufsda-spectra-bkg-inc`` — compare background vs increment spectra for a single experiment


Analysis Increment Spectra (CTRL vs EXP)
----------------------------------------

This diagnostic compares the spectral variance of analysis increments
from two experiments (e.g., CTRL vs EXP).

.. code-block:: bash

    ufsda-spectra-ana-inc config/spectra_ana_inc.yaml


Background vs Increment Spectra
-------------------------------

This diagnostic compares the background spectrum with the increment
spectrum for a single experiment.

.. code-block:: bash

    ufsda-spectra-bkg-inc config/spectra_bkg_inc.yaml


Example Figure
--------------

.. figure:: _static/images/spectra/bkg_T_inc_L75.png
   :width: 90%
   :align: center

   Background and increment spectra for temperature at model level 75.
   The increment spectrum shows how analysis updates redistribute
   variance across spatial scales relative to the background. Enhanced
   small‑scale variance indicates localized corrections, while reduced
   high‑wavenumber variance indicates smoother increments.


NICAS Length‑Scale Example
--------------------------

The NICAS experiment modifies the static background‑error covariance by
increasing the horizontal correlation length scale in the SABER NICAS
operator. A larger length scale produces broader spatial correlations and
smoother increments, which appear in the spectra as enhanced
low‑wavenumber variance and reduced high‑wavenumber variance.

.. figure:: _static/images/spectra/T_inc_ctrl_vs_length-scale_spectra_L75.png
   :width: 90%
   :align: center

   Comparison of CTRL and NICAS length‑scale experiments for temperature
   increments at level 75. The NICAS experiment uses a larger horizontal
   correlation length scale, broadening the background‑error
   correlations and shifting variance toward large scales.


YAML Example
------------

Below is a minimal YAML configuration for CTRL vs EXP increment spectra:

.. code-block:: yaml

    experiment:
      ctrl: CTRL
      exp: EXP
      ctrl_increment: ctrl_inc.nc4
      exp_increment: exp_inc.nc4

    output:
      directory: spectra/
      plots: true

For background vs increment spectra:

.. code-block:: yaml

    experiment:
      name: CTRL
      background: bkg.nc4
      increment: inc.nc4

    output:
      directory: spectra/
      plots: true
