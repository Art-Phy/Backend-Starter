
All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and this project adheres to Semantic Versioning.

### [0.1.0] - 2026-06-06

#### Added

- Created the initial project structure.
- Added the main `backend_starter` package.
- Added the first CLI entry point.
- Implemented automatic generation of a basic backend project structure.
- Added automatic creation of:
  - `README.md`
  - `CHANGELOG.md`
  - `requirements.txt`
  - `.gitignore`
  - `src/<project_name>/__init__.py`
  - `tests/__init__.py`
- Separated the application into dedicated modules:
  - `cli.py`
  - `generator.py`
  - `templates.py`

#### Notes

This release provides the first functional version of Backend Starter, capable of generating a basic Python backend project structure from the command line.