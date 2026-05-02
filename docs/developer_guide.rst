Developer Guide
===============

This guide describes the architecture, coding standards, and development
workflow for the UFS DA Diagnostics Toolkit. It is intended for
developers extending the toolkit with new diagnostics, plotting
utilities, CLI tools, or API modules.


Architecture
------------

The package is organized into four primary subsystems:

- ``spectra`` — spectral diagnostics (power spectra, spectral ratios)
- ``increment`` — increment maps, stitched global maps, zonal means
- ``obs`` — observation‑space diagnostics (bias, RMS, NRMS, QC, ATMS)
- ``logs`` — JEDI log parsing and chi‑squared consistency checks

Each subsystem contains:

- a **core engine** (computations and data processing)
- **plotting utilities** (figures used by CLI tools and user scripts)
- **CLI entry points** (YAML‑driven workflows)
- **API modules** (importable functions for custom workflows)

All subsystems follow the same design pattern:  
**YAML in → core engine → plotting → structured outputs**.


Coding Standards
----------------

- Use **Google‑style docstrings** for all public functions and classes.
- **Type hints are required** for all function arguments and return types.
- Keep module paths short and avoid deep nesting.
- All workflows must be **YAML‑driven** for reproducibility.
- CLI tools must be registered in ``pyproject.toml`` under
  ``[project.scripts]``.
- Plotting functions must be isolated in ``ufs_da_diagnostics.plots``.
- Use NumPy‑style naming for arrays (e.g., ``k``, ``E``, ``d_b``, ``d_a``).
- Keep functions small and modular; avoid monolithic scripts.


Adding a New Diagnostic Subsystem
---------------------------------

To add a new diagnostic subsystem:

1. **Create a new package** under ``ufs_da_diagnostics/``  
   Example: ``ufs_da_diagnostics/newdiag/``

2. **Add core engine modules**  
   Implement data loading, computation, and aggregation.

3. **Add plotting utilities**  
   Place all figures under ``ufs_da_diagnostics.plots``.

4. **Add a CLI entry point**  
   Register in ``pyproject.toml``:

   .. code-block:: toml

       [project.scripts]
       ufsda-newdiag = "ufs_da_diagnostics.newdiag.cli:main"

5. **Add API documentation**  
   Create ``docs/api/newdiag.rst`` with ``autodoc`` and ``autosummary``.

6. **Add usage documentation**  
   Create ``docs/usage_newdiag.rst`` with YAML examples and CLI usage.

7. **Add example figures**  
   Place PNGs under:

   ``docs/_static/images/newdiag/``

8. **Update the index**  
   Add the new page to ``docs/index.rst``.


Image and Documentation Standards
---------------------------------

- All images must be placed under:

  ``docs/_static/images/<subsystem>/``

  Example:

  - ``_static/images/spectra/``
  - ``_static/images/obs/``
  - ``_static/images/increment/``

- Filenames must be lowercase, descriptive, and underscore‑separated.
- Use ``.. figure::`` directives with captions that explain the
  scientific meaning of the figure.
- Use **Mermaid diagrams** where helpful for architecture or workflow
  visualization.
- Keep documentation pages short, modular, and cross‑referenced using
  ``:ref:``.


Testing and Validation
----------------------

- All new diagnostics must be tested with at least one real FV3‑JEDI
  experiment.
- Validate spectra, RMS statistics, and log‑derived metrics against known
  results.
- Ensure CLI tools run end‑to‑end using only the YAML file.
- Confirm that all plots render correctly in Sphinx and on ReadTheDocs.


Contributing
------------

Contributions should follow the modular design of the existing
subsystems. New diagnostics should integrate cleanly with the YAML‑driven
workflow, plotting utilities, and documentation structure described
above.
