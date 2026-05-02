Spectral Diagnostics API
========================

The spectral diagnostics subsystem provides tools for computing
wavenumber spectra, spectral ratios, and multi-panel summaries from
FV3-JEDI increment and background fields.

This API reference documents the core spectral engine as well as the
two driver modules used by the CLI tools:

- ``ufsda-spectra-ana-inc`` — compare analysis increments (CTRL vs EXP)
- ``ufsda-spectra-bkg-inc`` — compare background vs increment (single experiment)


Modules
-------

.. automodule:: ufs_da_diagnostics.spectra.spectra_core
    :members:
    :undoc-members:
    :show-inheritance:
    :noindex:

.. automodule:: ufs_da_diagnostics.spectra.spectra_analysis_tiles
    :members:
    :undoc-members:
    :noindex:

.. automodule:: ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc
    :members:
    :undoc-members:
    :noindex:


Function Summary
----------------

.. autosummary::
   :toctree: generated/
   :nosignatures:

   ufs_da_diagnostics.spectra.spectra_core.SpectraCore
   ufs_da_diagnostics.spectra.spectra_analysis_tiles.main
   ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc.main


Detailed API
------------

Core Engine
~~~~~~~~~~~

.. autoclass:: ufs_da_diagnostics.spectra.spectra_core.SpectraCore
   :members:
   :undoc-members:
   :show-inheritance:
   :no-index:


Analysis Increment Driver
~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.spectra.spectra_analysis_tiles.main
   :no-index:


Background vs Increment Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc.main
   :no-index:
