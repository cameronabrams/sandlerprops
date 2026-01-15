.. _installation:

Installation
============

Requirements
------------

sandlerprops requires:

* Python 3.7 or later
* NumPy
* SciPy
* pint
* sandlermisc (for some general utilities)
* sandlerprops (for compound critical properties and heat-capacity data)

Install from PyPI
-----------------

The easiest way to install sandlerprops is using pip:

.. code-block:: bash

   pip install sandlerprops

This will automatically install all required dependencies.

Install from Source
-------------------

To install the latest development version from GitHub:

.. code-block:: bash

   git clone https://github.com/cameronabrams/sandlerprops.git
   cd sandlerprops
   pip install -e .

This installs the package in "editable" mode, which is useful for development.

Verify Installation
-------------------

To verify that sandlerprops is installed correctly, run:

.. code-block:: bash

   sandlerprops --help

You should see the help message for the command-line interface.

Alternatively, from Python:

.. code-block:: python

   import sandlerprops
   print(sandlerprops.__version__)

Updating
--------

To update to the latest version:

.. code-block:: bash

   pip install --upgrade sandlerprops

Uninstalling
------------

To remove sandlerprops:

.. code-block:: bash

   pip uninstall sandlerprops
