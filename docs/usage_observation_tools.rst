Observation Diagnostic Tools
============================

Running the CLI Tool
--------------------

.. code-block:: bash

    ufsda-obs-diagnostic config/obs_diag.yaml


YAML Configuration
------------------

.. code-block:: yaml

    input:
      ioda_file: obs.nc4

    output:
      directory: obs_diag/
      plots: true

    variables:
      - brightness_temperature
      - humidity


Outputs
-------

- scalar histograms
- vector histograms
- ATMS scan-position plots
- QC summaries
