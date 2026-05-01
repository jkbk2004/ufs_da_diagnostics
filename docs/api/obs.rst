Observation Utilities API
=========================

This module provides lightweight helpers for inspecting IODA observation
files. These utilities are useful when preparing YAML configurations for
observation diagnostics or when exploring file structure.

.. automodule:: ufs_da_diagnostics.obs.utils
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

List variables in an IODA file:

.. code-block:: python

    from ufs_da_diagnostics.obs.utils import list_variables
    print(list_variables("diag_t.nc"))

List groups:

.. code-block:: python

    from ufs_da_diagnostics.obs.utils import list_groups
    print(list_groups("diag_t.nc"))

See :doc:`../usage_observation_tools` for the full workflow.

