Log Diagnostics API
===================

The log diagnostics subsystem provides tools for parsing a full JEDI
variational DA log file and extracting structured diagnostic information.
This includes configuration metadata, observation counts, Jo evolution,
cost-function convergence, departures, and observation error statistics.

The primary implementation is located in:

``ufs_da_diagnostics/log/parse_jedi_log.py``

This page documents all public functions in the module.


Module Contents
---------------

.. automodule:: ufs_da_diagnostics.log.parse_jedi_log
    :no-undoc-members:
    :no-private-members:
    :no-special-members:


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

parse_configuration
~~~~~~~~~~~~~~~~~~~
.. autofunction:: parse_configuration

parse_obs_counts
~~~~~~~~~~~~~~~~
.. autofunction:: parse_obs_counts

parse_jo_evolution
~~~~~~~~~~~~~~~~~~
.. autofunction:: parse_jo_evolution

parse_cost_convergence
~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: parse_cost_convergence

parse_departures
~~~~~~~~~~~~~~~~
.. autofunction:: parse_departures

parse_obs_errors
~~~~~~~~~~~~~~~~
.. autofunction:: parse_obs_errors

generate_report
~~~~~~~~~~~~~~~
.. autofunction:: generate_report

main
~~~~
.. autofunction:: main
