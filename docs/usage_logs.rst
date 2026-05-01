Using Log Diagnostics
=====================

The log diagnostics subsystem parses a full JEDI variational DA log and
extracts structured diagnostics.

Running the CLI Tool
--------------------

.. code-block:: bash

    ufsda-log-diagnostic config/log_diag.yaml


YAML Configuration
------------------

.. code-block:: yaml

    input:
      log_file: jedi.log

    output:
      directory: log_diagnostics/
      save_json: true
      plots: true


Outputs
-------

- ``config.json`` — extracted configuration
- ``obs_counts.json`` — observation counts
- ``jo_evolution.png`` — Jo evolution plot
- ``cost_convergence.png`` — cost function plot
- ``departures.json`` — departures summary
