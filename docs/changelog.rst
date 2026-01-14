.. _changelog:

Changelog
=========

All notable changes to sandlerprops will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[0.4.0] - 2026-01-14
--------------------

Added
~~~~~

* full reimplementation

Documentation
~~~~~~~~~~~~~

* Readthedocs setup

[0.1.0] - 2024-02-27
--------------------

Added
~~~~~

* Initial release of sandlerprops
* Python API for programmatic use

Documentation
~~~~~~~~~~~~~

* README with installation and usage examples
* MIT License
* Basic package metadata


Breaking Changes Policy
-----------------------

sandlerprops follows semantic versioning:

* **MAJOR** version (X.0.0): Incompatible API changes
* **MINOR** version (0.X.0): New functionality, backwards-compatible
* **PATCH** version (0.0.X): Bug fixes, backwards-compatible

Deprecation Warnings
--------------------

No features are currently deprecated.

When features are deprecated, they will:

1. Remain functional in current MAJOR version
2. Issue ``DeprecationWarning`` when used
3. Include migration instructions in warning message
4. Be documented in this changelog
5. Be removed in next MAJOR version


Contributing to Changelog
--------------------------

When contributing changes:

1. Add entry under ``[Unreleased]`` section
2. Use appropriate subsection (Added/Changed/Deprecated/Removed/Fixed/Security)
3. Write concise, user-focused descriptions
4. Link to relevant issue/PR numbers
5. Maintainers will organize entries during release

Example entry::

   [Unreleased]
   ------------
   
   Added
   ~~~~~
   * Output to CSV
   * vapor pressure calculations at specified temperture
   
   Fixed
   ~~~~~
   * Incorrect units in heat capacity data

See Also
--------

* :doc:`contributing` - How to contribute
* `GitHub Releases <https://github.com/cameronabrams/sandlerprops/releases>`_ - Release notes
* `GitHub Issues <https://github.com/cameronabrams/sandlerprops/issues>`_ - Bug reports and feature requests
