"""
Spectral Diagnostics Core Engine
================================

This module implements the core spectral diagnostics used by both
``ufsda-spectra-ana-inc`` (CTRL vs EXP increment comparison) and
``ufsda-spectra-bkg-inc`` (background vs increment comparison).

The ``SpectraCore`` class provides:

- FV3 cubed-sphere tile loading
- Grid loading and corner → center conversion
- Cubed-sphere → global lat/lon regridding
- 1D isotropic spectra
- Vertical variance profiles
- 2D spectral ratios

This module contains **no plotting** and **no CLI logic** — it is a
pure computational engine used by the two driver scripts.
"""

import xarray as xr
import numpy as np
from scipy.interpolate import griddata


class SpectraCore:
    """
    Core FV3-JEDI spectral diagnostics engine.

    This class provides the computational backend for spectral analysis
    workflows, including:

    - Loading FV3 cubed-sphere tiles
    - Loading FV3 grid geometry and converting corner → center points
    - Regridding cubed-sphere tiles to a global lat/lon mesh
    - Computing isotropic 1D wavenumber spectra
    - Computing vertical variance profiles
    - Computing 2D spectral ratios (EXP / CTRL)

    Parameters
    ----------
    varname : str, optional
        Name of the variable to extract from FV3 increment files.
        Default is ``"T_inc"``.
    grid_prefix : str, optional
        Prefix for FV3 grid files, e.g. ``"./C96_grid.tile"``.
    suffix : str, optional
        File suffix for both grid and data files (default ``".nc"``).

    Notes
    -----
    This class does **not** perform any plotting. Plotting is handled by
    the driver modules:

    - ``spectra_analysis_tiles.py`` (ANA–INC)
    - ``spectra_analysis_bkg_inc.py`` (BKG–INC)
    """

    def __init__(self, varname="T_inc", grid_prefix="./C96_grid.tile", suffix=".nc"):
        self.varname = varname
        self.grid_prefix = grid_prefix
        self.suffix = suffix
        self.nlevels = None
        self.k = None

    # ----------------------------------------------------------------------
    def load_tile(self, prefix, tile, level):
        """Load a single FV3 cubed-sphere tile for a given vertical level.

        Parameters
        ----------
        prefix : str
            File prefix for the tile, e.g. ``"/path/to/atminc.tile"``.
        tile : int
            Tile number (1–6).
        level : int
            Vertical level index.

        Returns
        -------
        numpy.ndarray
            2D array of the requested variable at the given level.

        Notes
        -----
        Assumes FV3-JEDI tile files follow the naming pattern::

            <prefix><tile><suffix>
        """
        ds = xr.open_dataset(f"{prefix}{tile}{self.suffix}", engine="netcdf4")
        return ds[self.varname].isel(Time=0, zaxis_1=level).values

    # ----------------------------------------------------------------------
    def load_grid(self, tile):
        """Load FV3 grid geometry and compute cell-center coordinates.

        Parameters
        ----------
        tile : int
            Tile number (1–6).

        Returns
        -------
        lon_c : numpy.ndarray
            2D array of cell-center longitudes.
        lat_c : numpy.ndarray
            2D array of cell-center latitudes.

        Notes
        -----
        FV3 grid files store corner coordinates. This method converts
        them to cell centers using a 4-point average.
        """
        grid = xr.open_dataset(f"{self.grid_prefix}{tile}{self.suffix}", engine="netcdf4")
        lon = grid["x"].values
        lat = grid["y"].values

        lon_c = 0.25 * (lon[0:-1:2, 0:-1:2] +
                        lon[1::2,   0:-1:2] +
                        lon[0:-1:2, 1::2] +
                        lon[1::2,   1::2])

        lat_c = 0.25 * (lat[0:-1:2, 0:-1:2] +
                        lat[1::2,   0:-1:2] +
                        lat[0:-1:2, 1::2] +
                        lat[1::2,   1::2])

        lon_c = (lon_c + 180) % 360 - 180
        return lon_c, lat_c

    # ----------------------------------------------------------------------
    def build_global(self, prefix, level):
        """Regrid all six FV3 tiles to a global lat/lon mesh for one level.

        Parameters
        ----------
        prefix : str
            Tile file prefix, e.g. ``"/path/to/atminc.tile"``.
        level : int
            Vertical level index.

        Returns
        -------
        Lon : numpy.ndarray
            2D longitude meshgrid (regular lat/lon grid).
        Lat : numpy.ndarray
            2D latitude meshgrid.
        field_interp : numpy.ndarray
            2D field interpolated onto the global mesh.

        Notes
        -----
        - Tile fields are flattened and concatenated.
        - ``scipy.interpolate.griddata`` performs nearest-neighbor
          interpolation onto a regular 1°×1° grid.
        """
        fields, lons, lats = [], [], []

        for t in range(1, 7):
            fields.append(self.load_tile(prefix, t, level))
            lon_c, lat_c = self.load_grid(t)
            lons.append(l_c := lon_c)
            lats.append(lat_c)

        field_global = np.concatenate([f.flatten() for f in fields])
        lon_global   = np.concatenate([g.flatten() for g in lons])
        lat_global   = np.concatenate([g.flatten() for g in lats])

        lon_new = np.linspace(-180, 180, 360)
        lat_new = np.linspace(-90, 90, 181)
        Lon, Lat = np.meshgrid(lon_new, lat_new)

        field_interp = griddata(
            points=(lon_global, lat_global),
            values=field_global,
            xi=(Lon, Lat),
            method="nearest"
        )

        return Lon, Lat, field_interp

    # ----------------------------------------------------------------------
    def build_global_all_levels(self, prefix, nlevels):
        """Regrid all vertical levels for a given experiment.

        Parameters
        ----------
        prefix : str
            Tile file prefix.
        nlevels : int
            Number of vertical levels.

        Returns
        -------
        Lon : numpy.ndarray
            2D longitude meshgrid.
        Lat : numpy.ndarray
            2D latitude meshgrid.
        fields : numpy.ndarray
            3D array of shape ``(nlevels, ny, nx)`` containing all levels.
        """
        Lon, Lat = None, None
        fields = []

        for lev in range(nlevels):
            Lon, Lat, field = self.build_global(prefix, lev)
            fields.append(field)

        return Lon, Lat, np.array(fields)

    # ----------------------------------------------------------------------
    def isotropic_spectrum(self, field):
        """Compute the 1D isotropic wavenumber spectrum of a 2D field.

        Parameters
        ----------
        field : numpy.ndarray
            2D field on a regular lat/lon grid.

        Returns
        -------
        numpy.ndarray
            1D isotropic spectrum ``E(k)``.

        Notes
        -----
        - Uses 2D FFT with ``fftshift``.
        - Computes radial bins in wavenumber space.
        - Returns energy density averaged over annuli.
        """
        ny, nx = field.shape

        F = np.fft.fftshift(np.fft.fft2(field))
        P = np.abs(F)**2

        ky = np.fft.fftshift(np.fft.fftfreq(ny))
        kx = np.fft.fftshift(np.fft.fftfreq(nx))
        KX, KY = np.meshgrid(kx, ky)
        K = np.sqrt(KX**2 + KY**2)

        kmax = int(np.sqrt((nx/2)**2 + (ny/2)**2))
        spectrum = np.zeros(kmax)
        counts = np.zeros(kmax)

        for i in range(ny):
            for j in range(nx):
                k = int(K[i, j] * kmax)
                if k < kmax:
                    spectrum[k] += P[i, j]
                    counts[k] += 1

        return spectrum / np.maximum(counts, 1)

    # ----------------------------------------------------------------------
    def load_fields(self, ctrl_prefix, exp_prefix, nlevels=127):
        """Load CTRL and EXP fields for all vertical levels and compute spectra.

        Parameters
        ----------
        ctrl_prefix : str
            File prefix for CTRL increment tiles.
        exp_prefix : str
            File prefix for EXP increment tiles.
        nlevels : int, optional
            Number of vertical levels to load (default 127).

        Returns
        -------
        None
            Results are stored as attributes:
            - ``CTRL_3D`` : 3D array of CTRL fields
            - ``EXP_3D``  : 3D array of EXP fields
            - ``spec_ctrl_all`` : spectra for all CTRL levels
            - ``spec_exp_all``  : spectra for all EXP levels
            - ``spec_ratio_all`` : EXP/CTRL spectral ratio
            - ``k`` : wavenumber array
        """
        self.Lon, self.Lat, self.CTRL_3D = self.build_global_all_levels(ctrl_prefix, nlevels)
        _,      _,      self.EXP_3D  = self.build_global_all_levels(exp_prefix,  nlevels)

        self.nlevels = nlevels

        self.spec_ctrl_all = []
        self.spec_exp_all  = []

        for lev in range(nlevels):
            sc = self.isotropic_spectrum(self.CTRL_3D[lev])
            se = self.isotropic_spectrum(self.EXP_3D[lev])
            self.spec_ctrl_all.append(sc)
            self.spec_exp_all.append(se)

        self.spec_ctrl_all = np.array(self.spec_ctrl_all)
        self.spec_exp_all  = np.array(self.spec_exp_all)

        self.spec_ratio_all = self.spec_exp_all / np.maximum(self.spec_ctrl_all, 1e-12)
        self.k = np.arange(self.spec_ctrl_all.shape[1])

    # ----------------------------------------------------------------------
    def variance_profile(self):
        """Compute vertical variance ratio (EXP / CTRL).

        Returns
        -------
        numpy.ndarray
            1D array of variance ratios for each vertical level.

        Notes
        -----
        Variance is computed as the sum of the isotropic spectrum
        across all wavenumbers.
        """
        var_ctrl = self.spec_ctrl_all.sum(axis=1)
        var_exp  = self.spec_exp_all.sum(axis=1)
        return var_exp / np.maximum(var_ctrl, 1e-12)

    # ----------------------------------------------------------------------
    def spectral_ratio_2d(self):
        """Return the full 2D spectral ratio array (EXP / CTRL).

        Returns
        -------
        numpy.ndarray
            2D array of shape ``(nlevels, nk)`` containing spectral ratios.
        """
        return self.spec_ratio_all
