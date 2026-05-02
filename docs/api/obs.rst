Observation Diagnostics Driver API
==================================

The ``obs_diagnostic`` module provides the command-line interface for
running observation diagnostics. It loads a YAML configuration file and
dispatches all requested diagnostics through the
``ObsDiagPlotter`` orchestrator in ``ufs_da_diagnostics.plots``.

This module does not implement diagnostics directly; it only provides
the CLI wrapper.


Module
------

.. automodule:: ufs_da_diagnostics.obs.obs_diagnostic
    :members:
    :undoc-members:
    :show-inheritance:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    parse_args
    main


Detailed API
------------

Argument Parsing
~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.parse_args


CLI Entry Point
~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.main
