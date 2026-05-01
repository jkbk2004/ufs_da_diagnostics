Developer Guide
===============

This guide describes the architecture, coding standards, and development
workflow for the diagnostics toolkit.

Architecture
------------

The package is organized into four subsystems:

- ``spectra`` — spectral diagnostics
- ``increment`` — increment maps and zonal means
- ``obs`` — observation diagnostics
- ``logs`` — log parsing

Each subsystem contains:

- a core engine
- optional drivers
- plotting utilities
- CLI entry points


Coding Standards
----------------

- Google-style docstrings
- type hints required
- avoid long module paths
- YAML-driven workflows
- modular CLI entry points


Adding a New Subsystem
----------------------

1. Create a new package under ``ufs_da_diagnostics/``
2. Add core engine modules
3. Add plotting utilities
4. Add CLI entry point in ``pyproject.toml``
5. Add API documentation
6. Add usage documentation


Documentation Standards
-----------------------

- Use autosummary for function lists
- Use autodoc for detailed API
- Include Mermaid diagrams where helpful
- Keep pages short and modular
