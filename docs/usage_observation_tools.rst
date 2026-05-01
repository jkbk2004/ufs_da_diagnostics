Observation Tools
=================

This page provides a unified overview of all observation‑related tools in
``ufs-da-diagnostics``. These tools support both **diagnostic plotting**
(ATMS, scalar, vector) and **observation file inspection** (metadata,
variables, groups).

The observation diagnostics are YAML‑driven and executed through the
command‑line driver. The inspection utilities are Python‑level helpers
for exploring IODA files.


Running Observation Diagnostics
-------------------------------

Use the ``obs_diagnostic`` driver to run all requested diagnostics:

.. code-block:: bash

    python -m ufs_da_diagnostics.obs.obs_diagnostic --yaml obs_plots.yaml

The ``--yaml`` argument points to a configuration file describing the
observations to process.


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


Observation File Inspection
---------------------------

The package also includes utilities for inspecting IODA files:

.. code-block:: python

    from ufs_da_diagnostics.obs.utils import list_variables, list_groups

    vars = list_variables("diag_t.nc")
    print(vars)

    groups = list_groups("diag_t.nc")
    print(groups)

These tools help users understand the structure of IODA files before
configuring diagnostics.


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

This completes the unified workflow for observation‑space tools.

Example YAML
------------

An example observation diagnostics configuration is available in:

``ufs_da_diagnostics/examples/diag_fv3-jedi_obs.yaml``

It demonstrates:

- ATMS, scalar, and vector diagnostics
- Histogram and statistics settings
- Scan-position and latitude-binned plots
- Output directory configuration

Use this file as a starting point for your observation workflows.


