# Changelog

All notable changes to sandlerprops will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2026-03-06

### Added

- `Cp_mean` method for calculating mean heat capacity over a temperature range.

## [0.6.1] - 2026-02-03

### Fixed

- Minor `Compound` class fix; dependency metadata updated.

## [0.6.0] - 2026-02-03

### Added

- `Pvap` estimation method.
- Use pint unit registry `ureg` from `sandlermisc.constants`.

## [0.5.0] - 2026-01-15

### Changed

- All quantities with units are now `pint.Quantity` objects.

## [0.4.0] - 2026-01-14

### Changed

- Full reimplementation of properties API.

### Added

- ReadTheDocs documentation setup.

## [0.3.1] - 2026-01-01

### Fixed

- Properties database corrections; test suite updates.

## [0.3.0] - 2026-01-01

### Added

- `Compound` class; expanded CLI; properties database updates.

## [0.2.2] - 2025-12-31

### Changed

- README and package metadata updates.

## [0.2.1] - 2025-12-31

### Changed

- `properties.py` refactored; CLI cleanup.

## [0.1.0] - 2025-12-24

### Added

- Initial release of sandlerprops.
- Python API for programmatic use.