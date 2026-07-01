"""
Templates related to AI assistants and project context.

These files are optional and generated only when using the --ai flag.
"""


AGENT_TEMPLATE = """
# AGENTS.md

# Development Guidelines

---

# Core Principles

---

# Project Structure

Unless the project requires otherwise:

Typical layout:

---

# Language Style

---

# Documentation

Documentation is considered part of the project.

README:

- Written in "add your language".

CHANGELOG:

- Written in "add your language".
- Follow Keep a Changelog.

Release Notes:

- Written in "add your language".

Code comments:

- Written in English.

Docstrings:

- Written in English.

---

# Git Workflow

Use GitFlow.

Typical branches:

```text
feature/*
bugfix/*
hotfix/*
release/*
```

Never work directly on `main`.

Commits must be written in English.

---

# Testing

Before considering a task finished:

---

# Dependencies

---

# CLI Applications

For CLI projects:

---

# APIs

---

# Database

Prefer:

---

# Docker

When Docker is used:

---

# Documentation Quality

When modifying documentation:

- Keep examples updated.
- Keep version numbers consistent.
- Update `CHANGELOG.md` when needed.
- Update `README.md` if features, commands or setup steps change.
- Prefer clear explanations over overly technical wording.

---

# Agent Behaviour

When making suggestions:

When editing code:

If multiple solutions exist:

If an improvement could be beneficial but was not requested:

Never introduce unnecessary complexity.

---

# Philosophy

"""


PROJECT_TEMPLATE = """
# PROJECT.md

# Project Context

This document describes the purpose, current status and technical context of this repository.

It is intended to help developers and AI agents understand the project before making changes.

---

# Overview

Short description of what this project does.

---

# Goal

Main purpose of the project.

---

# Current Status

Current project status:

```text
Planning / Development / Stable / Maintenance
```

Current version:

```text
v0.1.0
```

---

# Tech Stack

Main technologies used in this project:

---

# Architecture

Brief explanation of how the project is organized.

Explain the responsibility of the main modules:

---

# Main Commands

Useful commands for development.

Create virtual environment:

Activate virtual environment:

Install project in editable mode:

Run tests:

Run the application:

---

# Development Notes

Important decisions, constraints or conventions specific to this project.

---

# Roadmap

## Planned

- Add future task here.

## In Progress

- Add current task here.

## Completed

- Initial project structure.
- Basic documentation.

---

# Known Issues

Known limitations or pending fixes.

- No known issues yet.

---

# Release Notes Context

Use this section to keep track of important changes that may be useful when preparing a release.

---

# Notes for Future Agents

Before making changes:

- Read `AGENTS.md`.
- Read this file.
- Check the current project status.
- Prefer small, focused changes.
- Keep the roadmap updated when relevant.
"""