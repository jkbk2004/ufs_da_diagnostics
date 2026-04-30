Quickstart
==========

This page provides a fast introduction to installing and using the
``ufs-da-diagnostics`` package. The goal is to help you run your first
diagnostic plot or increment visualization in just a few steps.

Prerequisites
-------------

You will need:

- Python 3.9 or newer
- A working scientific Python environment (conda recommended)
- Required dependencies: ``numpy``, ``matplotlib``, ``xarray``,
  ``netCDF4``, ``cartopy``, ``pyyaml``

If you installed the package using ``pip install .`` these dependencies
are already handled.

Basic Usage
-----------

Once installed, you can import the package and access all diagnostics
modules through the unified namespace:

.. code-block:: python

    import ufs_da_diagnostics as udiag

    # Example: run an observation diagnostic plotter
    udiag.obs_diag_plotter("path/to/obs/diagnostic/file.nc")

    # Example: run an increment tile plot
    udiag.increment_maps_tiles("path/to/increment/file.nc")

Modules Overview
----------------

The package is organized into two main components:

- **plots/** — ATMS, H(x), innovations, spectra, QC, and other
  observation-based diagnostics
- **increment/** — increment visualization tools such as tile-based
  increment maps

To explore available functions:

.. code-block:: python

    import ufs_da_diagnostics as udiag
    dir(udiag)

Next Steps
----------

- See :doc:`installation` for setup instructions
- See :doc:`api/plots` for observation diagnostics API
- See :doc:`api/increment` for increment diagnostics API
