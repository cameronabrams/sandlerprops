.. _quickstart:

Quick Start Guide
=================

This guide will get you up and running with sandlerprops in just a few minutes.

Basic Concepts
--------------

sandlerprops provides access to the pure-component properties database from Sandler's *Chemical, Biochemical, and Engineering Thermodynamics* (5th edition).  Data was extracted from the Microsoft Access Database that was packaged with its `properties` VisualBasic application.

The following pure-component properties are available:

* Critical properties (T\ :sub:`c`, P\ :sub:`c`, V\ :sub:`c`)
* Acentric factor (ω)
* Antoine coefficients for vapor pressure correlations
* Heat capacity correlation coefficients
* Heat of vaporization correlation coefficients
* Elemental composition and molecular weight
* Standard-state enthalpy and entropy of formation at 298.15 K and 1 bar
* Dipole moment (select compounds only)

In the properties database, temperatures are in Kelvin (K), pressures are in bar, volumes are in cm³/mol, enthalpies are in J/mol, and entropies are in J/mol-K.  All quantities with units are represented as :class:`pint.Quantity` objects.

First Properties Look-up
------------------------

Let's look up the pure-component propertiesof methane:

From the Command Line
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sandlerprops show methane

Output::

   Properties of methane (index 116):
   ----------------------------------------
      No             : 116
      Formula        : CH4
      Name           : methane
      Molwt          : 16.043 g / mol
      Tfp            : 90.700 K
      Tb             : 111.600 K
      Tc             : 190.400 K
      Pc             : 46.000 bar
      Vc             : 99.200 m ** 3 / mol
      Zc             : 0.288
      Omega          : 0.011
      Dipm           : 0.000 D
      CpA            : 19.25
      CpB            : 0.05213
      CpC            : 1.197e-05
      CpD            : -1.132e-08
      dHf            : -74900.000 J / mol
      dGf            : -50870.000 J / mol
      Eq             : 1
      VpA            : -6.004
      VpB            : 1.119
      VpC            : -0.8341
      VpD            : -1.228
      Tmin           : 91.000 K
      Tmax           : 190.400 K
      Lden           : 0.425
      Tden           : 112.000 K

From Python
~~~~~~~~~~~

.. code-block:: python

   from sandlerprops import get_database

   P = get_database()

   result = P.get_compound("methane")
   print(f"Critical temperature: {result.Tc}")
   print(f"Critical pressure: {result.Pc}")
   print(f"Acentric factor: {result.Omega}")
   print(f"Molecular weight: {result.Molwt}")

Within the Python API, the **Compound** object returned by `get_compound` has attributes corresponding to all available pure-component properties, as well as the atomic composition
of the compound.

.. code-block:: python

   # Accessing atomic composition
   composition = result.atomdict
   for element, count in composition.items():
       print(f"{element}: {count}")

Next Steps
----------

* Learn more about the :doc:`cli` for advanced command-line usage
* Check the :doc:`api/API` for complete API documentation
