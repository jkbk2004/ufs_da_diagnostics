"""
Utility Functions for Plotting
==============================

This module contains small helper utilities used across the plotting
subsystem. These functions are intentionally lightweight and focused on
common numerical operations needed by diagnostics plots.
"""


def symmetric_limits(data):
    """
    Compute symmetric colorbar limits around zero.

    This function is typically used for increment maps or any plot
    requiring a diverging colormap centered at zero. It ensures that the
    minimum and maximum limits are symmetric, based on the largest
    absolute value in the data.

    Parameters
    ----------
    data : numpy.ndarray
        Input array from which to compute symmetric limits.

    Returns
    -------
    tuple of float
        ``(vmin, vmax)`` where both are symmetric around zero.

    Examples
    --------
    >>> symmetric_limits(np.array([-3, 1, 2]))
    (-3, 3)

    Notes
    -----
    - ``data.min()`` and ``data.max()`` must be finite.
    - The function does not modify the input array.
    """
    m = max(abs(data.min()), abs(data.max()))
    return -m, m
