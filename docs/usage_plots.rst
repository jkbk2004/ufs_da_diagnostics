Using Plotting Tools
====================

The plotting subsystem provides reusable utilities for generating
diagnostic figures used throughout the toolkit. All CLI tools call these
plotting functions automatically, but they can also be used directly in
custom workflows. For examples of the resulting figures, see
:ref:`Diagnostics Overview <diagnostics_overview>`.


Scalar Histogram Example
------------------------

The scalar histogram plotter is used for variables such as temperature,
humidity, and pressure.

.. code-block:: python

    from ufs_da_diagnostics.plots.scalar_hist import plot_scalar_hist

    # data: 1D array of values
    plot_scalar_hist(data, variable="t")


Vector Histogram Example
------------------------

Vector histograms are used for wind components (u, v).

.. code-block:: python

    from ufs_da_diagnostics.plots.vector_hist import plot_vector_hist

    plot_vector_hist(u_data, v_data, variable="wind")


Spectra Plot Example
--------------------

The spectra plotter generates 1D power spectra for background fields,
increments, and experiment‑to‑experiment comparisons.

.. code-block:: python

    from ufs_da_diagnostics.plots.spectra_plots import plot_spectra_1d

    # k: wavenumbers
    # E: spectral energy
    plot_spectra_1d(k, E)


ATMS Extended Statistics Example
--------------------------------

The extended RMS statistics plotter is used for channel‑wise satellite
diagnostics such as ATMS.

.. code-block:: python

    from ufs_da_diagnostics.plots.atms_stats_extended import plot_atms_stats

    plot_atms_stats(stats_dict, channels=range(1, 23))


Scan‑Position Bias Example
--------------------------

ATMS scan‑position diagnostics visualize cross‑track bias patterns.

.. code-block:: python

    from ufs_da_diagnostics.plots.atms_scanpos import plot_scan_position_bias

    plot_scan_position_bias(scanpos_data)
