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

    SpectraCore
    SpectraCore.compute_spectrum
    SpectraCore.compute_vertical_variance
    SpectraCore.load_field

    main  # from spectra_analysis_tiles
    main  # from spectra_analysis_bkg_inc


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

spectra_analysis_bkg_inc
~~~~~~~~~~~~~~~~~~~~~~~~
.. autofunction:: ufs_da_diagnostics.spectra.spectra_analysis_bkg_inc.main
