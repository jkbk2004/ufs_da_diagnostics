Increment Maps Diagnostics
==========================

The *increment maps* diagnostic generates horizontal FV3 6‑tile maps and
zonal‑mean cross‑sections of analysis increments from FV3-JEDI. It supports:

- Single‑experiment increment maps
- Two‑experiment CTRL–EXP–DIFF comparison maps
- Zonal‑mean (latitude × level) diagnostics
- YAML‑driven configuration
- Command-line execution via ``ufsda-inc-maps``

This tool is implemented in:

``ufs_da_diagnostics.increment.increment_maps_tiles``

and exposed through the CLI entry point:

.. code-block:: bash

    ufsda-inc-maps --yaml diag_fv3-jedi-tiles.yaml


Overview
--------

Increment maps visualize the spatial structure of analysis increments
(e.g., ``T_inc``, ``u_inc``, ``v_inc``, ``sphum_inc``) on the native FV3
cubed-sphere grid. The diagnostic reads tile files:

``prefix.tile1.nc`` … ``prefix.tile6.nc``

and stitches them into global lat/lon maps using the FV3 grid files.

The tool also computes zonal means (lat × level) for each variable and level.


YAML Configuration
------------------

The diagnostic is fully driven by a YAML configuration file. A typical example:

.. code-block:: yaml

    vars:
      - T_inc
      - sphum_inc
      - u_inc
      - v_inc

    levels:
      - 126
      - 75

    experiments:
      - name: ctrl
        prefix: "/path/to/ctrl/ufsda.t00z.atminc.cubed_sphere_grid.tile"

      - name: exp
        prefix: "/path/to/exp/ufsda.t00z.atminc.cubed_sphere_grid.tile"

    grid:
      prefix: "/path/to/C96_grid.tile"

    output_dir: "./plot-outputs"

Configuration Fields
~~~~~~~~~~~~~~~~~~~~

``vars``  
    List of increment variables to plot.

``levels``  
    Vertical levels (FV3 native indices).

``experiments``  
    One or two experiments.  
    - One experiment → single-case maps  
    - Two experiments → CTRL, EXP, DIFF maps

``prefix``  
    Path prefix for tile files (tile1.nc … tile6.nc).

``grid.prefix``  
    Path prefix for FV3 grid files.

``output_dir``  
    Directory where PNG files are written.


Single-Experiment Workflow
--------------------------

If the YAML file contains **one experiment**, the tool generates one map per
variable and level:

.. code-block:: bash

    ufsda-inc-maps --yaml diag_fv3-jedi-tiles.yaml

Output files:

``T_inc_L126_ctrl.png``  
``T_inc_L75_ctrl.png``  
``u_inc_L126_ctrl.png``  
…

Each figure contains:

- 6 FV3 tiles stitched into a global lat/lon map
- PlateCarree projection
- Horizontal colorbar
- Title with variable, level, and experiment name


Two-Experiment CTRL–EXP–DIFF Workflow
-------------------------------------

If the YAML file contains **two experiments**, the tool generates:

- CTRL map
- EXP map
- DIFF map (EXP − CTRL)

Example:

.. code-block:: bash

    ufsda-inc-maps --yaml diag_fv3-jedi-tiles.yaml

Output files:

``T_inc_L126_ctrl.png``  
``T_inc_L126_exp.png``  
``T_inc_L126_diff.png``  

Colorbars are normalized across all three panels for consistent comparison.


Zonal-Mean Diagnostics
----------------------

For each variable and level, the tool computes a zonal mean:

``zm(lat, level) = mean over longitude``

Output files:

``T_inc_L126_ctrl_zonal_mean.png``  
``T_inc_L126_exp_zonal_mean.png``  
``T_inc_L126_diff_zonal_mean.png``  

Features:

- Latitude × level cross-section
- Log-pressure or model-level vertical axis
- Shared colorbar across CTRL–EXP–DIFF
- Useful for diagnosing vertical increment structure


Command-Line Usage
------------------

Basic usage:

.. code-block:: bash

    ufsda-inc-maps --yaml diag.yaml

Specify output directory override:

.. code-block:: bash

    ufsda-inc-maps --yaml diag.yaml --outdir results/

Run in batch mode (HPC):

.. code-block:: bash

    srun -n 1 ufsda-inc-maps --yaml diag.yaml


Python API Usage
----------------

Although the CLI is recommended, the module can be used directly:

.. code-block:: python

    from ufs_da_diagnostics.increment.increment_maps_tiles import main, load_yaml_config

    config = load_yaml_config("diag.yaml")
    # The main() function handles full execution when run via CLI.


Output Files
------------

The diagnostic produces:

- Global increment maps (PNG)
- Zonal-mean cross-sections (PNG)
- One file per variable × level × experiment

All outputs are written to ``output_dir``.


Summary
-------

The increment maps diagnostic provides a fast, flexible way to visualize
analysis increments from FV3-JEDI. With YAML-driven configuration and a
simple CLI interface, it integrates cleanly into UFS-DA workflows and HPC
batch pipelines.


Example YAML
------------

A complete example YAML for increment diagnostics is included in:

``ufs_da_diagnostics/examples/diag_fv3-jedi-tiles.yaml``

This file demonstrates:

- Tile-based increment maps
- Dual-experiment comparisons
- Zonal-mean diagnostics
- Output directory structure

Use it as a template for your own increment workflows.


