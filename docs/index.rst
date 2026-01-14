.. sandlerprops documentation master file

sandlerprops
=============

.. image:: https://img.shields.io/pypi/v/sandlerprops.svg
   :target: https://pypi.org/project/sandlerprops/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/sandlerprops.svg
   :target: https://pypi.org/project/sandlerprops/
   :alt: Python versions

Digitized pure-component properties database from Sandler's 5th edition
-----------------------------------------------------------------------

**sandlerprops** implements a Python interface to pure-component properties database found in *Chemical, Biochemical, and Engineering Thermodynamics* (5th edition) by Stan Sandler (Wiley, USA). 

.. warning::
   This package should be used for **educational purposes only**.

Features
--------

* Given a compound name recongized by the database, retrieve:

  * Critical properties (T\ :sub:`c`, P\ :sub:`c`, V\ :sub:`c`)
  * Acentric factor (ω)
  * Antoine coefficients for vapor pressure correlations
  * Heat capacity correlation coefficients
  * Heat of vaporization correlation coefficients
  * Elemental composition and molecular weight
  * Standard-state enthalpy and entropy of formation at 298.15 K and 1 bar

Quick Start
-----------

Installation::

   pip install sandlerprops

Basic usage from the command line::

   sandlerprops show methane

Basic usage from Python:

.. code-block:: python

   from sandlerprops import get_database
   P = get_database()
   result = P.get_compound("methane")
   print(f"Critical temperature: {result.Tc} K")
   print(f"Critical pressure: {result.Pc} bar")
   print(f"Acentric factor: {result.omega}")
   print(f"Molecular weight: {result.Molwt} g/mol")
   
Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide
   
   installation
   quickstart
   cli

.. toctree::
   :maxdepth: 2
   :caption: API Reference
   
   api/API.rst

.. toctree::
   :maxdepth: 1
   :caption: Developer Guide
   
   contributing
   changelog

License
=======

This project is licensed under the MIT License - see the LICENSE file for details.

Citation
========

If you use this package for academic work, please cite:

* Sandler, S. (2017). *Chemical, Biochemical, and Engineering Thermodynamics* (5th ed.). Wiley.

Contact
=======

Cameron F. Abrams - cfa22@drexel.edu

GitHub: https://github.com/cameronabrams/sandlerprops
