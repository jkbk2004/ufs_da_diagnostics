"""
Universal Loader Utilities for Observation Diagnostics
======================================================

This module provides robust, observation‑type‑agnostic loader functions
for reading OMB, OMA, QC, ObsValue, and hofx fields from FV3‑JEDI /
IODA‑formatted diagnostics files.

The loaders are designed to handle:

- ATMS radiances
- GNSSRO bending angles
- SATWND / SCATWND winds
- Conventional observations (e.g., PS, T, Q)
- Legacy IODA formats (ombg/oman, innov1, DerivedMetaData/Innovation)
- Masked arrays, object arrays, and missing groups

All returned arrays are converted to **float64** with invalid entries
replaced by **NaN**, ensuring downstream plotting code never crashes due
to dtype inconsistencies.

This module is the foundation for all histogram, stats, and QC‑filtered
diagnostics.
"""

import numpy as np


# ----------------------------------------------------------------------
# Numeric conversion helper
# ----------------------------------------------------------------------

def to_numeric_safe(arr):
    """
    Convert any ObsValue/hofx/OMB/OMA array to ``float64`` safely.

    This function handles:
    - masked arrays (``.filled(np.nan)``)
    - object arrays (element‑wise conversion)
    - invalid entries (converted to ``NaN``)
    - arbitrary shapes

    Parameters
    ----------
    arr : array-like or None
        Input array from diagnostics file.

    Returns
    -------
    numpy.ndarray or None
        Float64 array with invalid entries replaced by NaN.
        Returns ``None`` if input is ``None``.

    Notes
    -----
    - This function is essential for GNSSRO, where some fields may be
      stored as object arrays.
    - Ensures downstream code can always call ``np.isfinite()`` safely.
    """
    if arr is None:
        return None

    # Masked arrays → fill with NaN
    if hasattr(arr, "filled"):
        arr = arr.filled(np.nan)

    arr = np.array(arr)

    # Object arrays → element-wise conversion
    if arr.dtype == object:
        out = np.empty(arr.shape, dtype="float64")
        for idx, v in np.ndenumerate(arr):
            try:
                out[idx] = float(v)
            except Exception:
                out[idx] = np.nan
        return out

    return arr.astype("float64")


# ----------------------------------------------------------------------
# QC loader
# ----------------------------------------------------------------------

def load_qc_universal(f, varname):
    """
    Universal QC loader with multi-group fallback.

    Priority order:
      1. EffectiveQC2
      2. EffectiveQC1
      3. EffectiveQC0
      4. EffectiveQC
      5. ObsDiag
      6. QualityControl
      7. FortranQC

    Behavior
    --------
    - If a QC group exists but the variable is missing → return all-valid QC.
    - If no QC groups exist → return all-valid QC.
    - QC arrays are returned as ``int32``.

    Parameters
    ----------
    f : netCDF4.Dataset
        Diagnostics file handle.
    varname : str
        Observation variable name.

    Returns
    -------
    numpy.ndarray
        QC array of shape (Location,) or broadcastable to (Location, Channel).

    Notes
    -----
    - All-valid QC means ``QC == 0`` everywhere.
    - This loader supports both IODA-v1 and IODA-v2 conventions.
    """
    qc_groups = [
        "EffectiveQC2",
        "EffectiveQC1",
        "EffectiveQC0",
        "EffectiveQC",
        "ObsDiag",
        "QualityControl",
        "FortranQC",
    ]

    for grp in qc_groups:
        if grp in f.groups:
            g = f.groups[grp]

            # Standard IODA-v2 layout
            if varname in g.variables:
                return to_numeric_safe(g.variables[varname][:]).astype("int32")

            # IODA-v1 style: varname@group
            alt = f"{varname}@{grp}"
            if alt in f.variables:
                return to_numeric_safe(f[alt][:]).astype("int32")

            # Group exists but variable missing → all-valid QC
            nloc = f.dimensions["Location"].size
            return np.zeros(nloc, dtype="int32")

    # No QC groups found → all-valid QC
    nloc = f.dimensions["Location"].size
    return np.zeros(nloc, dtype="int32")


# ----------------------------------------------------------------------
# ObsValue loader
# ----------------------------------------------------------------------

def load_obsvalue(f, varname):
    """
    Load ObsValue for a given variable.

    Parameters
    ----------
    f : netCDF4.Dataset
        Diagnostics file.
    varname : str
        Variable name.

    Returns
    -------
    numpy.ndarray or None
        Float64 ObsValue array, or ``None`` if missing.
    """
    if "ObsValue" in f.groups and varname in f.groups["ObsValue"].variables:
        return to_numeric_safe(f.groups["ObsValue"].variables[varname][:])
    return None


# ----------------------------------------------------------------------
# hofx loader
# ----------------------------------------------------------------------

def load_hofx(f, varname):
    """
    Load hofx (hofx0 group).

    Parameters
    ----------
    f : netCDF4.Dataset
        Diagnostics file.
    varname : str
        Variable name.

    Returns
    -------
    numpy.ndarray or None
        Float64 hofx array, or ``None`` if missing.
    """
    if "hofx0" in f.groups and varname in f.groups["hofx0"].variables:
        return to_numeric_safe(f.groups["hofx0"].variables[varname][:])
    return None


# ----------------------------------------------------------------------
# OMB loader
# ----------------------------------------------------------------------

def load_omb(f, varname):
    """
    Universal OMB loader.

    Priority
    --------
      1. ``ombg/<varname>``  
         (ATMS, GNSSRO, SATWND, SCATWND, CONVENTIONAL_PS)
      2. ``innov1/<varname>``  
         (some IODA-v1 formats)
      3. ``DerivedMetaData/Innovation``  
         (fallback, e.g., ATMS)

    Parameters
    ----------
    f : netCDF4.Dataset
        Diagnostics file.
    varname : str
        Variable name.

    Returns
    -------
    numpy.ndarray or None
        Float64 OMB array, or ``None`` if not found.
    """
    if "ombg" in f.groups and varname in f.groups["ombg"].variables:
        return to_numeric_safe(f.groups["ombg"].variables[varname][:])

    if "innov1" in f.groups and varname in f.groups["innov1"].variables:
        return to_numeric_safe(f.groups["innov1"].variables[varname][:])

    if "DerivedMetaData" in f.groups and "Innovation" in f.groups["DerivedMetaData"].variables:
        return to_numeric_safe(f.groups["DerivedMetaData"].variables["Innovation"][:])

    return None


# ----------------------------------------------------------------------
# OMA loader
# ----------------------------------------------------------------------

def load_oma_explicit(f, varname):
    """
    Universal OMA loader.

    Priority
    --------
      1. ``oman/<varname>``  
         (ATMS, GNSSRO, SATWND, SCATWND, CONVENTIONAL_PS)
      2. ``ObsValue - hofx``  
         (fallback for formats without explicit OMA)

    Parameters
    ----------
    f : netCDF4.Dataset
        Diagnostics file.
    varname : str
        Variable name.

    Returns
    -------
    numpy.ndarray or None
        Float64 OMA array, or ``None`` if not computable.
    """
    if "oman" in f.groups and varname in f.groups["oman"].variables:
        return to_numeric_safe(f.groups["oman"].variables[varname][:])

    obs = load_obsvalue(f, varname)
    hofx = load_hofx(f, varname)
    if obs is None or hofx is None:
        return None

    return to_numeric_safe(obs - hofx)


# ----------------------------------------------------------------------
# Backward compatibility aliases
# ----------------------------------------------------------------------

load_qc_any = load_qc_universal
load_omb_any = load_omb
load_oma_any = load_oma_explicit
load_obs_any = load_obsvalue

