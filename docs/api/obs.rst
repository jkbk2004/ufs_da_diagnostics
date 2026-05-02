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
    :noindex:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.obs.obs_diagnostic.parse_args
    ufs_da_diagnostics.obs.obs_diagnostic.main


Detailed API
------------

Argument Parsing
~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.parse_args
   :no-index:


CLI Entry Point
~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.obs.obs_diagnostic.main
   :no-index:
