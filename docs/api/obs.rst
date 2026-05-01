Observation Utilities API
=========================

This page documents the observation‑inspection utilities included in
``ufs-da-diagnostics``. These tools provide lightweight helpers for
exploring IODA observation files, including variable listings, group
structure, and metadata inspection.

These utilities are useful when preparing YAML configurations for
observation diagnostics.


.. automodule:: ufs_da_diagnostics.obs.utils
   :members:
   :undoc-members:
   :show-inheritance:


Example
-------

List variables in an IODA diagnostics file:

.. code-block:: python

    from ufs_da_diagnostics.obs.utils import list_variables

    vars = list_variables("diag_t.nc")
    print(vars)


List groups:

.. code-block:: python

    from ufs_da_diagnostics.obs.utils import list_groups

    groups = list_groups("diag_t.nc")
    print(groups)


Notes
-----

- Utilities are read‑only and do not modify files.
- All functions return Python lists or dictionaries for easy use.
- These tools complement the YAML‑driven diagnostics driver documented in
  :doc:`../usage_observation_tools`.
