.. _usage_observation_tools:

Using Observation Diagnostics
=============================

The observation diagnostics subsystem provides tools for analyzing
observation departures, QC behavior, channel‑wise statistics, and
observation‑space performance of the data assimilation system. These
diagnostics complement the increment and spectral diagnostics by
quantifying how well the background and analysis fields fit the
observations. For the mathematical formulation and example figures, see
:ref:`Diagnostics Overview <diagnostics_overview>`.


Running the CLI Tool
--------------------

The main driver for observation‑space diagnostics is:

.. code-block:: bash

    ufsda-obs-diagnostic config/obs_diag.yaml

This tool computes O–B and O–A departures, bias, RMS, normalized RMS,
bias‑corrected RMS, QC‑filtered statistics, and channel‑wise summaries
for satellite and conventional observations.


Example Figure
--------------

.. figure:: _static/images/obs/atms_stats_extended.png
   :width: 90%
   :align: center

   Extended ATMS observation‑space diagnostics showing O–B and O–A bias,
   RMS, normalized RMS, bias‑corrected RMS, and analysis improvement
   metrics. These statistics quantify systematic error, total error,
   random error, and the degree to which the analysis reduces
   observation‑space departures.


YAML Configuration
------------------

A minimal YAML configuration for observation diagnostics:

.. code-block:: yaml

    input:
      ioda_file: obs.nc4
      hofx_bkg: hofx_bkg.nc4
      hofx_ana: hofx_ana.nc4

    output:
      directory: obs_diag/
      plots: true

    variables:
      - brightness_temperature
      - humidity


Outputs
-------

- ``scalar_hist/`` — scalar variable histograms (e.g., temperature, humidity)
- ``vector_hist/`` — vector component histograms (e.g., wind components)
- ``scanpos/`` — ATMS scan‑position bias diagnostics
- ``qc/`` — QC summaries and filtered statistics
- ``plots/`` — extended RMS and bias figures

These diagnostics provide a detailed view of observation‑space
performance and complement the increment and spectral diagnostics.
