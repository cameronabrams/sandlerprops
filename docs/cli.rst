.. _cli:

Command-Line Interface
======================

sandlerprops provides a command-line interface (CLI) for quick queries of the properties database without writing Python code.  It also provides a rudimentary search function to find compounds by name.

Overview
--------

The CLI has three main subcommands:

* ``show``: Show pure-component properties from the database for a specific compound
* ``showprops``: List all available properties in the database with units and descriptions
* ``find``: Search for compounds by name

Global Options
--------------

.. code-block:: bash

   sandlerprops --help

Shows general help and lists available subcommands. (Note that ``-h`` is reserved for enthalpy inputs.)  

.. code-block:: bash

   sandlerprops --version

Displays the installed version of sandlerprops.

``show`` Command
-----------------

Show pure-component properties from the database for a specific compound.

Syntax
~~~~~~

.. code-block:: bash

   sandlerprops show [compound-name]

Examples
~~~~~~~~

**Basic look-up:**  Methane:

.. code-block:: bash

   sandlerprops show methane

Output::

   Properties of methane (index 116):
   ----------------------------------------
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

**Search by name**: Find all compounds that match "eth":

.. code-block:: bash

   sandlerprops find eth

Output::

   eth not found.  Here are similars:
   ethane
   ethanol
   methane
   menthol
   ethylene
   methylal
   methanol
   thymol
   ketene
   ethyl amine

Units Reference
---------------

The CLI uses units as-provided in the database.  Below is a reference table of common properties and their units.

=================== ==================
Property            Unit
=================== ==================
Temperature (T)     Kelvin (K)
Mass (m)            Gram (g)
Volume (V)          m³
Pressure (P)        Bar 
Molar volume (v)    m³/mol
Enthalpy (H)        J/mol
Entropy (S)         J/(mol-K)
Heat capacity (Cp)  J/(mol-K)
=================== ==================

``showprops`` Command
-----------------------

List all available properties in the database with units and descriptions.

Syntax
~~~~~~

.. code-block:: bash

   sandlerprops showprops

Output:: 

   Property      Units   Description
   --------------------------------------------------
         No              Unique compound number
      Formula              Empirical formula
         Name              Unique compound name
      Molwt      g/mol   Molecular weight in g/mol
         Tfp          K   Triple point temperature in K
         Tb          K   Boiling point temperature in K
         Tc          K   Critical temperature in K
         Pc        bar   Critical pressure in bar
         Vc     m3/mol   Critical volume in m3/mol
         Zc              Critical compressibility
      Omega              Acentric factor
         Dipm              DIPM
         CpA    J/mol-K   Ideal gas heat capacity coeff 1
         CpB   J/mol-K2   Ideal gas heat capacity coeff 2
         CpC   J/mol-K3   Ideal gas heat capacity coeff 3
         CpD   J/mol-K4   Ideal gas heat capacity coeff 4
         dHf      J/mol   Ideal gas enthalpy of formation at 298.15 K
         dGf      J/mol   Ideal gas entropy of formation at 298.15 K
         Eq              Vapor pressure equation type number
         VpA              Vapor pressure coeff 1
         VpB              Vapor pressure coeff 2
         VpC              Vapor pressure coeff 3
         VpD              Vapor pressure coeff 4
         Tmin          K   Vapor pressure temperature range min
         Tmax          K   Vapor pressure temperature range max
         Lden              Liquid density at Tden
         Tden              Temperature at which liquid density is measured