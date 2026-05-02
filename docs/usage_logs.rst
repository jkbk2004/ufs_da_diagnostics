Using Log Diagnostics
=====================

The log diagnostics subsystem parses a full JEDI variational DA log and
extracts structured diagnostics including configuration metadata,
observation counts, Jo evolution, cost‑function convergence, departures,
and chi‑squared consistency information. These diagnostics complement
the increment, spectra, and observation‑space tools by providing insight
into the internal behavior of the variational minimization. For a
high‑level description, see :ref:`Diagnostics Overview
<diagnostics_overview>`.


Running the CLI Tool
--------------------

The main driver for log parsing is:

.. code-block:: bash

    ufsda-log-diagnostic config/log_diag.yaml

This tool scans the entire JEDI log file and extracts structured
diagnostic fields, producing JSON summaries and optional plots.


Chi‑Squared Consistency Check
-----------------------------

The log parser extracts Jo, Jb, and total cost values at each iteration
and computes the chi‑squared consistency metric:

.. math::

    \chi^2 = \frac{\mathrm{Jo}}{p}

where :math:`p` is the number of assimilated observations. Values near
unity indicate consistency between observation errors, background
errors, and the resulting analysis increments.


YAML Configuration
------------------

A minimal YAML configuration for log diagnostics:

.. code-block:: yaml

    input:
      log_file: jedi.log

    output:
      directory: log_diagnostics/
      save_json: true
      plots: true


Outputs
-------

- ``config.json`` — extracted configuration metadata  
- ``obs_counts.json`` — observation counts by type and channel  
- ``jo_evolution.png`` — Jo evolution across minimization iterations  
- ``cost_convergence.png`` — total cost, Jb, and Jo convergence  
- ``departures.json`` — O–B and O–A departure summaries  
- ``chi2.json`` — chi‑squared consistency diagnostics  

These outputs provide a structured view of the variational minimization
and help diagnose issues related to observation errors, background
errors, and convergence behavior.
