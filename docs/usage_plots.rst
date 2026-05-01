Observation Diagnostics — Usage Guide
=====================================

This page describes how to run the observation‑level diagnostics included
in ``ufs_da_diagnostics``. These tools generate histograms, statistics,
and specialized diagnostics for ATMS, scalar, and vector observations
from FV3‑JEDI IODA diagnostic files.

The workflow is YAML‑driven and uses the ``ObsDiagPlotter`` orchestrator.


Basic Workflow
--------------

1. Prepare a YAML configuration describing the observations to process.
2. Run the plotting driver (Python script or notebook).
3. Plots are written into the specified output directory.

All diagnostics automatically apply QC filtering and handle IODA
variations (ombg/oman, innov1, DerivedMetaData, etc.).


Example YAML Configuration
--------------------------

Below is a minimal example covering ATMS, scalar, and vector observations:

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


Running the Diagnostics
-----------------------

Use the ``ObsDiagPlotter`` class to execute all requested diagnostics:

.. code-block:: python

    import yaml
    from ufs_da_diagnostics.plots.obs_diag_plotter import ObsDiagPlotter

    with open("obs_plots.yaml") as f:
        config = yaml.safe_load(f)

    plotter = ObsDiagPlotter(config)
    plotter.run()

This will:

- Open each diagnostics file
- Detect the observation type
- Run the requested diagnostics
- Save plots into the specified output directories


ATMS Diagnostics
----------------

ATMS supports the full suite of diagnostics:

- Per‑channel histograms (QC2)
- Mean/Std statistics
- Extended statistics (RMS, NRMS, BC‑RMS)
- Scan‑position diagnostics
- Latitude‑binned diagnostics

Example output:

.. image:: _static/example_atms_stats.png
   :width: 600


Scalar Diagnostics
------------------

Scalar observations (e.g., radiosonde temperature) produce:

- OMB histogram (QC2)
- If OMB is missing (e.g., GNSSRO), an ObsValue histogram is produced instead.

Example:

.. image:: _static/example_scalar_hist.png
   :width: 500


Vector Diagnostics
------------------

Vector observations (SATWND, SCATWND, or any 2‑component variable) produce:

- U‑component histogram
- V‑component histogram

Both appear in a single figure.

Example:

.. image:: _static/example_vector_hist.png
   :width: 600


Output Directory Structure
--------------------------

A typical output directory may look like:

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

- All diagnostics use QC2 filtering unless otherwise noted.
- Missing OMB/OMA fields are handled gracefully.
- ATMS channel shading and legends follow NOAA conventions.
- KDE curves are drawn only when statistically meaningful.

This completes the basic usage workflow for observation diagnostics.
