#!/usr/bin/env python3
"""
ANA–INC Spectral Diagnostics Driver
===================================

This script performs spectral diagnostics comparing **analysis increments**
from two experiments (CTRL vs EXP). It is the backend for the CLI entry point:

    ufsda-spectra-ana-inc --yaml spectra_ana_inc.yaml

The workflow:

1. Read YAML configuration
2. Load increment fields for CTRL and EXP
3. Regrid cubed-sphere tiles → global lat/lon
4. Compute isotropic spectra for selected variables and levels
5. Generate comparison plots:
   - CTRL spectrum
   - EXP spectrum
   - CTRL vs EXP comparison
   - Spectral ratio (EXP / CTRL)
   - Optional NICAS length-scale overlay

This driver uses:
- ``SpectraCore`` for computation
- ``SpectraPlotter`` for visualization
"""

import argparse
import yaml
import os

from .spectra_core import SpectraCore
from ..plots.spectra_plots import SpectraPlotter


def main():
    """Run ANA–INC spectral diagnostics from a YAML configuration file.

    This function implements the full workflow for comparing analysis
    increments between two experiments (CTRL vs EXP). It is invoked by
    the CLI entry point ``ufsda-spectra-ana-inc``.

    YAML Configuration
    ------------------
    Expected structure:

    .. code-block:: yaml

        experiments:
          - name: ctrl
            prefix: "/path/to/ctrl/atminc.tile"
          - name: exp
            prefix: "/path/to/exp/atminc.tile"

        grid:
          prefix: "/path/to/C96_grid.tile"

        vars: [u_inc, v_inc, T_inc]
        levels: [126, 75, 50]

        output_dir: "./spectra_ana_inc"
        nicas_length_scale: 120000  # optional

    Parameters
    ----------
    None

    Returns
    -------
    None
        All output is written to PNG files in the configured output directory.

    Notes
    -----
    - This driver always loads **127 vertical levels** internally, even if
      only a subset is plotted.
    - ``SpectraCore`` performs all computation; this script only orchestrates
      workflow and plotting.
    - The NICAS length scale (if provided) is passed through to the plotter
      for optional overlay.
    """
    parser = argparse.ArgumentParser(description="FV3-JEDI Spectral Diagnostics (Tiles → Lat/Lon)")
    parser.add_argument("--config", "--yaml", dest="config", required=True,
                        help="YAML configuration file")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)

    vars_list  = cfg["vars"]
    levels     = cfg["levels"]
    exps       = cfg["experiments"]
    outdir     = cfg.get("output_dir", "./plot-outputs")
    nicas_L    = cfg.get("nicas_length_scale", None)

    if "grid" in cfg and "prefix" in cfg["grid"]:
        grid_prefix = cfg["grid"]["prefix"]
    else:
        grid_prefix = cfg["grid_prefix"]

    os.makedirs(outdir, exist_ok=True)

    ctrl = exps[0]
    exp  = exps[1]

    ctrl_name   = ctrl["name"]
    ctrl_prefix = ctrl["prefix"]
    exp_name    = exp["name"]
    exp_prefix  = exp["prefix"]

    print("\n==============================================")
    print(" FV3-JEDI Spectral Diagnostics (Tiles → Lat/Lon)")
    print("==============================================")
    print(f" CTRL: {ctrl_name} → {ctrl_prefix}")
    print(f" EXP:  {exp_name} → {exp_prefix}")
    print(f" Vars: {vars_list}")
    print(f" Levels: {levels}")
    print(f" Grid prefix: {grid_prefix}")
    print(f" Output dir: {outdir}")
    print("==============================================\n")

    spec_plotter = SpectraPlotter()

    for var in vars_list:
        print(f"\n=== Processing variable: {var} ===")

        core = SpectraCore(varname=var, grid_prefix=grid_prefix)
        print("Loading global fields for all 127 levels...")
        core.load_fields(ctrl_prefix, exp_prefix, nlevels=127)

        for lev in levels:
            print(f"  → Level {lev}")

            outname = (
                f"{outdir}/"
                f"{var}_{ctrl_name}_vs_{exp_name}_spectra_L{lev}.png"
            )

            spec_plotter.plot_spectra(
                core, lev, ctrl_name, exp_name,
                fname=outname,
                nicas_length_scale=nicas_L
            )

    print("\nAll spectral diagnostics complete.\n")


if __name__ == "__main__":
    main()
