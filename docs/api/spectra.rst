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
    :no-undoc-members:
    :no-private-members:
    :no-special-members:

.. automodule:: ufs_da_diagnostics.spectra.spectra_analysis_tiles
    :no-undoc-members:
    :no-private-members:
    :no-special-members:

.. automodule:: ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc
    :no-undoc-members:
    :no-private-members:
    :no-special-members:


Function Summary
----------------

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ufs_da_diagnostics.spectra.spectra_core.SpectraCore
    ufs_da_diagnostics.spectra.spectra_core.SpectraCore.compute_spectrum
    ufs_da_diagnostics.spectra.spectra_core.SpectraCore.compute_vertical_variance
    ufs_da_diagnostics.spectra.spectra_core.SpectraCore.load_field

    ufs_da_diagnostics.spectra.spectra_analysis_tiles.main
    ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc.main


Detailed API
------------

SpectraCore
~~~~~~~~~~~
.. autoclass:: ufs_da_diagnostics.spectra.spectra_core.SpectraCore
    :members:
    :undoc-members:
    :show-inheritance:

spectra_analysis_tiles
~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: ufs_da_diagnostics.spectra.spectra_analysis_tiles.main
    :no-index:

spectra_analysis_bkg_inc
~~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc.main
    :no-index:


Full Source: spectra_analysis_bkg_inc.py
----------------------------------------

.. literalinclude:: ../../ufs_da_diagnostics/spectra/spectra_analysis_bkg_inc.py
   :language: python
   :linenos:
