Observation Diagnostics
=======================

This page describes how to run the observation‑space diagnostics included
in ``ufs-da-diagnostics``. These diagnostics generate histograms,
statistics, and specialized plots for ATMS, scalar, and vector
observations from FV3‑JEDI IODA diagnostic files.

All observation diagnostics are driven by a YAML configuration file and
executed using the command‑line driver.


Running the Driver
------------------

Use the ``obs_diagnostic`` driver to run all requested diagnostics:

.. code-block:: bash

    python -m ufs_da_diagnostics.obs.obs_diagnostic --yaml obs_plots.yaml

The ``--yaml`` argument is required and points to a configuration file
describing the observations to process.


YAML Configuration
------------------

A minimal example covering ATMS, scalar, and vector observations:

.. code-block:: yaml

    observations:
      - label: ATMS
        type: atms
        variable: brightness_temperature
        file: diag_atms.nc
        outdir: ./plots/atms
        diagnostics:
          hist: true
          stats: true
          extended: true
          scanpos: true
          latbins: true

      - label: Radiosonde T
        type: scalar
        variable: air_temperature
        file: diag_t.nc
        outdir: ./plots/sondes
        diagnostics:
          hist: true

      - label: Winds
        type: vector
        variable: windVector
        file: diag_wind.nc
        outdir: ./plots/winds
        diagnostics:
          hist: true

Each entry defines:

- ``label`` — name used in plot titles and filenames  
- ``type`` — ``atms``, ``scalar``, or ``vector``  
- ``variable`` — variable name inside the diagnostics file  
- ``file`` — path to the IODA diagnostics file  
- ``outdir`` — output directory for plots  
- ``diagnostics`` — which diagnostics to run  


Available Diagnostics
---------------------

ATMS
^^^^

- Channel histograms  
- Mean/Std statistics  
- Extended statistics (RMS, NRMS, BC‑RMS)  
- Scan‑position diagnostics  
- Latitude‑binned diagnostics  

Scalar
^^^^^^

- OMB histogram (QC2)  
- If OMB is missing, an ObsValue histogram is produced  

Vector
^^^^^^

- U‑component histogram  
- V‑component histogram  
- Both appear in a single figure  


Example Output Structure
------------------------

.. code-block:: text

    plots/
      atms/
        atms_ch01_hist.png
        atms_stats.png
        atms_stats_extended.png
        atms_scan_position_qc2.png
        atms_latbins_qc2.png

      sondes/
        radiosonde_t_hist.png

      winds/
        winds_vector_hist.png


Notes
-----

- QC2 filtering is applied automatically.
- Missing OMB/OMA fields are handled gracefully.
- ATMS shading and legends follow NOAA conventions.
- Vector diagnostics require 2‑component variables.

This completes the usage workflow for observation‑space diagnostics.

