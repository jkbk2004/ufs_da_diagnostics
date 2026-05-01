JEDI Log Diagnostics API
========================

The log diagnostics subsystem provides tools for parsing a full JEDI
variational DA log file and extracting structured diagnostic
information. This includes configuration metadata, observation counts,
Jo evolution, cost‑function convergence, departures, and observation
error statistics.

This page documents the full log‑parsing engine under
``ufs_da_diagnostics.logs``.


Modules
-------

.. automodule:: ufs_da_diagnostics.logs.parse_jedi_log
    :members:
    :undoc-members:
    :show-inheritance:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.logs.parse_jedi_log.parse_configuration
    ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_counts
    ufs_da_diagnostics.logs.parse_jedi_log.parse_jo_evolution
    ufs_da_diagnostics.logs.parse_jedi_log.parse_cost_convergence
    ufs_da_diagnostics.logs.parse_jedi_log.parse_departures
    ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_errors
    ufs_da_diagnostics.logs.parse_jedi_log.generate_report
    ufs_da_diagnostics.logs.parse_jedi_log.main


Detailed API
------------

Configuration Parsing
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_configuration


Observation Counts
~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_counts


Jo Evolution
~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_jo_evolution


Cost‑Function Convergence
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_cost_convergence


Departures
~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_departures


Observation Error Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_errors


Report Generation
~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.generate_report


CLI Entry Point
~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.main

