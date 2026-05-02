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
    :noindex:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    parse_configuration
    parse_obs_counts
    parse_jo_evolution
    parse_cost_convergence
    parse_departures
    parse_obs_errors
    generate_report
    main


Detailed API
------------

Configuration Parsing
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_configuration
   :no-index:

Observation Counts
~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_counts
   :no-index:

Jo Evolution
~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_jo_evolution
   :no-index:

Cost‑Function Convergence
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_cost_convergence
   :no-index:

Departures
~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_departures
   :no-index:

Observation Error Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.parse_obs_errors
   :no-index:

Report Generation
~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.generate_report
   :no-index:

CLI Entry Point
~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.logs.parse_jedi_log.main
   :no-index:
