# Codebase Overview - Legacy Image Processing Monolith

## Age
First release in 2014, last major functional update in 2018.

## Size
~35,000 LOC in Python 2.7 / early Python 3.5.

## Dependencies
- Python 2.7 / Python 3.5
- OpenCV 3.4
- Early versions of Pillow (PIL)
- MySQL 5.5 with custom SQL queries

## Issues
- **Lack of Test Coverage**: Zero unit or integration tests existing in the repository.
- **High Module Coupling**: Facial analysis, user authentication, and photo rendering are tightly coupled in monolithic scripts.
- **Deprecated Libraries**: Relies on unmaintained dependencies with known security vulnerabilities.
- **Synchronous Blocking I/O**: Heavy image processing blocks the main execution thread, causing performance bottlenecks.