Spectral Diagnostics
====================

The spectral diagnostics subsystem provides two complementary workflows:

1. **Analysis Increment Comparison (ANA–INC)**  
   Compare increment spectra between two experiments (CTRL vs EXP).

2. **Background vs Increment Spectra (BKG–INC)**  
   Compare background spectra against increment spectra for a single experiment.

Both workflows operate on FV3 native cubed-sphere tiles and produce
1D wavenumber spectra, spectral ratios, and optional multi-panel
summary figures.


Spectral Workflows
------------------

The subsystem provides two CLI drivers:

- ``ufsda-spectra-ana-inc``  
  Compare analysis increments from two experiments.

- ``ufsda-spectra-bkg-inc``  
  Compare background vs increment spectra for one experiment.

Each driver uses its own YAML configuration and produces different
diagnostic figures.


------------------------------------------------------------
Analysis Increment Comparison (ANA–INC)
------------------------------------------------------------

This workflow compares increment spectra between **two experiments**:

- CTRL increment (reference)
- EXP increment (test experiment)

It is commonly used to evaluate the impact of algorithmic changes,
observation configuration updates, or tuning experiments.

CLI Usage
~~~~~~~~~

.. code-block:: bash

    ufsda-spectra-ana-inc --yaml spectra_ana_inc.yaml

YAML Example
~~~~~~~~~~~~

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

    spectra:
      compute_ratio: true
      multi_panel: true

Generated Figures
~~~~~~~~~~~~~~~~~

1. **CTRL Spectrum**  
   ``<var>_L<lev>_ctrl.png``

2. **EXP Spectrum**  
   ``<var>_L<lev>_exp.png``

3. **CTRL | EXP | DIFF Comparison**  
   ``<var>_L<lev>_ctrl_vs_exp.png``

4. **Spectral Ratio (EXP / CTRL)**  
   ``<var>_L<lev>_ratio.png``

5. **Multi-Panel Summary**  
   ``spectra_summary_ana_inc.png``


------------------------------------------------------------
Background vs Increment Spectra (BKG–INC)
------------------------------------------------------------

This workflow compares:

- **Background field** (BKG)
- **Increment field** (INC)

for a **single experiment**.  
It is useful for understanding how increments modify the background
energy distribution across scales.

CLI Usage
~~~~~~~~~

.. code-block:: bash

    ufsda-spectra-bkg-inc --yaml spectra_bkg_inc.yaml

YAML Example
~~~~~~~~~~~~

.. code-block:: yaml

    experiment:
      name: exp
      bkg_prefix: "/path/to/bkg.tile"
      inc_prefix: "/path/to/atminc.tile"

    grid:
      prefix: "/path/to/C96_grid.tile"

    vars: [u, v, T]
    levels: [126, 75]

    output_dir: "./spectra_bkg_inc"

    spectra:
      compute_ratio: true
      multi_panel: true

Generated Figures
~~~~~~~~~~~~~~~~~

1. **Background Spectrum**  
   ``<var>_L<lev>_bkg.png``

2. **Increment Spectrum**  
   ``<var>_L<lev>_inc.png``

3. **BKG vs INC Comparison**  
   ``<var>_L<lev>_bkg_vs_inc.png``

4. **Spectral Ratio (INC / BKG)**  
   ``<var>_L<lev>_ratio.png``

5. **Multi-Panel Summary**  
   ``spectra_summary_bkg_inc.png``


Python API Usage
----------------

Both workflows rely on the same underlying spectral engine:

.. code-block:: python

    from ufs_da_diagnostics.spectra.spectra_core import SpectraCore

    core = SpectraCore(prefix="/path/to/atminc.tile",
                       grid_prefix="/path/to/grid.tile")

    k, E = core.compute_spectrum("u_inc", level=126)


File Locations
--------------

- ``ufs_da_diagnostics/spectra/spectra_core.py``  
- ``ufs_da_diagnostics/spectra/spectra_analysis_tiles.py``  
- ``ufs_da_diagnostics/spectra/spectra_analysis_bkg_inc.py``  
- ``ufs_da_diagnostics/spectra/`` (supporting modules)

CLI entry points (from ``pyproject.toml``):

- ``ufsda-spectra-ana-inc``
- ``ufsda-spectra-bkg-inc``


See Also
--------

- :doc:`../api/spectra`
- :doc:`../usage_increment`
- :doc:`usage_log`
- :doc:`usage_observation_tools`


Example YAML
------------

A ready-to-run background–increment spectra YAML is provided in:

``ufs_da_diagnostics/examples/diag_fv3-jedi-bkg_inc.yaml``

This example includes:

- Background and increment file definitions
- Variable selection
- 1D and 2D spectra settings
- Vertical variance diagnostics

You can adapt this file for your own spectral analysis.

