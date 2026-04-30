"""
Spectra diagnostics for UFS-DA.

Provides:
- SpectraCore: core FFT and spectra utilities
- spectra_analysis_tiles: tile-based spectra driver
- spectra_analysis_bkg_inc: background/increment spectra driver
"""

from .spectra_core import SpectraCore
from . import spectra_analysis_tiles
from . import spectra_analysis_bkg_inc

__all__ = [
    "SpectraCore",
    "spectra_analysis_tiles",
    "spectra_analysis_bkg_inc",
]
