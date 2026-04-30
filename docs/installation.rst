Installation
============

This page describes how to install the ``ufs-da-diagnostics`` package
from source. The package is designed to be lightweight and easy to
integrate into existing UFS-DA or FV3-JEDI workflows.

Install from Source
-------------------

Clone the repository:

.. code-block:: bash

    git clone https://github.com/jkbk2004/ufs-da-diagnostics.git
    cd ufs-da-diagnostics

Install using ``pip``:

.. code-block:: bash

    pip install .

This installs the package along with all required dependencies.

Editable Install (for development)
----------------------------------

If you plan to modify the diagnostics or contribute improvements, use:

.. code-block:: bash

    pip install -e .

This allows changes in the source tree to be reflected immediately
without reinstalling.

Dependencies
------------

The package requires:

- numpy
- matplotlib
- xarray
- netCDF4
- cartopy
- pyyaml

These are automatically installed when using ``pip install .``.

Testing the Installation
------------------------

To verify that the package is installed correctly:

.. code-block:: python

    import ufs_da_diagnostics as udiag
    print("Diagnostics package loaded:", udiag)

If no errors appear, the installation is successful.

Building Documentation
----------------------

To build the documentation locally:

.. code-block:: bash

    python -m sphinx -b html docs docs/_build/html

Open the generated HTML:

.. code-block:: bash

    docs/_build/html/index.html
