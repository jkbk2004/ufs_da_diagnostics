Observation Diagnostics Driver
==============================

This page describes how to run the observation‑level diagnostics using
the command‑line driver ``obs_diagnostic.py``. This tool reads a YAML
configuration file and generates histograms, statistics, and other
diagnostics for ATMS, scalar, and vector observations.

The driver is a thin wrapper around the ``ObsDiagPlotter`` orchestrator.


Overview
--------

The driver performs the following steps:

1. Reads a YAML configuration file.
2. Loads the observation diagnostics NetCDF files.
3. Dispatches diagnostics based on observation type:
   - ATMS radiances
   - Scalar observations (e.g., radiosonde temperature)
   - Vector observations (e.g., SATWND/SCATWND winds)
4. Writes plots into the specified output directories.

All QC handling, OMB/OMA loading, and plotting logic is handled
internally by the diagnostics subsystem.


Command‑Line Usage
------------------

Run the driver with:

.. code-block:: bash

    $ python -m ufs_da_diagnostics.obs.obs_diagnostic --yaml obs_plots.yaml

or, if installed as a script:

.. code-block:: bash

    $ obs_diagnostic.py --yaml obs_plots.yaml

The ``--yaml`` argument is required.


YAML Configuration
------------------

The YAML file controls all diagnostics. Example:

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


Driver Internals
----------------

The driver consists of two functions:

``parse_args()``  
    Parses the ``--yaml`` argument.

``main()``  
    Loads the YAML file, constructs an ``ObsDiagPlotter`` instance, and
    runs all diagnostics.

The driver does not contain plotting logic; it simply forwards the
configuration to the plotting subsystem.


Example Output
--------------

After running the driver, the output directory may look like:

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
- ATMS diagnostics include channel shading and group legends.
- Vector diagnostics require 2‑component variables.

This completes the usage instructions for the observation diagnostics driver.
