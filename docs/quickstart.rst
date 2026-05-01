
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
    print("Diagnostics package loaded:", udiag)

Diagnostics are organized into three major components:

- **Observation diagnostics** (ATMS, scalar, vector)
- **Increment diagnostics** (tile maps, zonal means)
- **Spectral diagnostics** (1D/2D spectra)


Running Observation Diagnostics
-------------------------------

Observation diagnostics are driven by a YAML configuration file. Example:

.. code-block:: yaml

    observations:
      - label: ATMS
        type: atms
        variable: brightness_temperature
        file: diag_atms.nc
        outdir: ./plots/atms
        diagnostics:
          hist: true
          stats: true

Save this as ``obs_plots.yaml`` and run:

.. code-block:: bash

    python -m ufs_da_diagnostics.obs.obs_diagnostic --yaml obs_plots.yaml

This will generate histograms, statistics, and other diagnostics in the
specified output directory.

See :doc:`usage_plots` for the full workflow.


Running Increment Diagnostics
-----------------------------

Increment maps are generated using the tile‑based increment plotter:

.. code-block:: bash

    python -m ufs_da_diagnostics.increment.increment_maps_tiles \
        --yaml increment_config.yaml

A minimal YAML example:

.. code-block:: yaml

    increments:
      file: fv3_increment.nc
      outdir: ./plots/increment
      variables: [u, v, t, ps]

See :doc:`usage_increment` for details.


Running Spectral Diagnostics
----------------------------

Spectral diagnostics use the ``SpectraPlotter`` class:

.. code-block:: python

    from ufs_da_diagnostics.plots.spectra_plots import SpectraPlotter

    plotter = SpectraPlotter()
    plotter.plot_spectra(core, level=50,
                         ctrl_name="CTRL",
                         exp_name="EXP",
                         fname="spectra_level50.png")

See :doc:`usage_spectra` for full examples.


Next Steps
----------

- See :doc:`installation` for setup instructions
- See :doc:`usage_plots` for observation diagnostics
- See :doc:`usage_increment` for increment diagnostics
- See :doc:`usage_spectra` for spectral diagnostics
- See :doc:`api/plots` and :doc:`api/increment` for API details


Example YAML Files
------------------

Example configuration files are included with the package under:

``ufs_da_diagnostics/examples/``

These provide ready-to-run templates for each diagnostics subsystem:

- ``diag_fv3-jedi-bkg_inc.yaml`` — Background–increment spectral diagnostics
- ``diag_fv3-jedi_obs.yaml`` — Observation-space diagnostics
- ``diag_fv3-jedi-tiles.yaml`` — Increment maps and zonal-mean diagnostics

You can copy and modify these files to match your workflow.

