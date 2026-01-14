.. _quickstart:

Quick Start Guide
=================

This guide will get you up and running with sandlerprops in just a few minutes.

Basic Concepts
--------------

sandlerprops provides access to the pure-component properties database from Sandler's *Chemical, Biochemical, and Engineering Thermodynamics* (5th edition) as well as implementations of several cubic equations of state (EOS) for calculating thermodynamic properties of pure substances.

The following pure-component properties are available:

* Critical properties (T\ :sub:`c`, P\ :sub:`c`, V\ :sub:`c`)
* Acentric factor (ω)
* Antoine coefficients for vapor pressure correlations
* Heat capacity correlation coefficients
* Heat of vaporization correlation coefficients
* Elemental composition and molecular weight
* Standard-state enthalpy and entropy of formation at 298.15 K and 1 bar

In the properties database, temperatures are in Kelvin (K), pressures are in bar, volumes are in cm³/mol, enthalpies are in J/mol, and entropies are in J/mol-K.

First Properties Look-up
------------------------

Let's look up the pure-component propertiesof methane:

From the Command Line
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sandlerprops show methane

Output::

   Properties of methane (index 116):
      No        : 116
      Formula   : CH4
      Name      : methane
      Molwt     :  16.043    g/mol
      Tfp       :  90.7      K
      Tb        :  111.6     K
      Tc        :  190.4     K
      Pc        :  46.00     bar
      Vc        :  99.200    m3/mol
      Zc        :  0.288
      Omega     :  0.011
      Dipm      : 0
      CpA       :  19.25     J/mol-K
      CpB       :  0.0521    J/mol-K2
      CpC       :  1.1970e-05 J/mol-K3
      CpD       : -1.1320e-08 J/mol-K4
      dHf       : -74900.0   J/mol
      dGf       : -50870.0   J/mol
      Eq        : 1
      VpA       : -6.00435
      VpB       :  1.11850
      VpC       : -0.83408
      VpD       : -1.22833
      Tmin      :  91.0      K
      Tmax      :  190.4     K
      Lden      :  0.425
      Tden      :  112.0

From Python
~~~~~~~~~~~

.. code-block:: python

   from sandlerprops import get_database

   P = get_database()

   result = P.get_compound("methane")
   print(f"Critical temperature: {result.Tc} K")
   print(f"Critical pressure: {result.Pc} bar")
   print(f"Acentric factor: {result.omega}")
   print(f"Molecular weight: {result.Molwt} g/mol")

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
