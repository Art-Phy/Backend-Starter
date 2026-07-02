
<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Project%20Generator-orange" />
  <img src="https://img.shields.io/badge/GitFlow-Automated-green" />
  <img src="https://img.shields.io/badge/VirtualEnv-Optional-success" />
  <img src="https://img.shields.io/badge/Installable-CLI-success" />
  <img src="https://img.shields.io/badge/AI%20Templates-Optional-blueviolet" />
  <img src="https://img.shields.io/badge/Version-v0.7.0-success" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

### Backend Starter

Backend Starter es una herramienta CLI desarrollada en Python para generar de forma automática la estructura inicial de un proyecto backend.

El objetivo es evitar repetir manualmente la creación de carpetas y archivos comunes cada vez que se inicia un nuevo proyecto.

#### Funcionalidades

- Creación automática de un nuevo proyecto backend.
- Generación de archivos base:
  - README.md
  - CHANGELOG.md
  - requirements.txt
  - .gitignore
  - AGENT.md
  - PROJECT.md
- Creación de estructura `src/`.
- Creación de paquete Python inicial.
- Creación de carpeta `tests/`.
- Inicialización automática de repositorio **Git**.
- Creación automática de rama **develop**.
- Creación opcional de entorno virtual mediante `--venv`.
- Generación opcional de `AGENT.md` y `PROJECT.md` mediante `--ai`.
- Ayuda integrada mediante `argparse`.
- Instalación como herramienta CLI mediante `pip install -e .`.
- Compatible con instalación mediante `pipx`.

#### Estructura generada

* Proyecto básico

```text
my_project/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── src/
│   └── my_project/
│       └── __init__.py
└── tests/
    └── __init__.py
```

* Con `--ai`:

```text
my_project/
├── README.md
├── CHANGELOG.md
├── AGENT.md
├── PROJECT.md
├── requirements.txt
├── .gitignore
├── src/
│   └── my_project/
│       └── __init__.py
└── tests/
    └── __init__.py
```

#### Instalación

##### Desarrollo

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e .
```

##### Uso recomendado

```bash
brew install pipx

pipx ensurepath

pipx install git+https://github.com/Art-Phy/backend-starter.git
```

#### Uso

Proyecto básico:

```bash
backend-starter my_project
```

Con entorno virtual:

```bash
backend-starter my_project --venv
```

Con documentación para IA:

```bash
backend-starter my_project --venv --ai
```

#### Objetivo del proyecto

Backend Starter nace como una herramienta para automatizar el arranque de proyectos backend en Python.

Continuará evolucionando con nuevas funcionalidades como:

- Plantillas para proyectos CLI.
- Plantillas para proyectos FastAPI.
- Integración con Docker.
- Integración con GitHub Actions.

#### Tecnologías

- Python 3
- pathlib
- argparse
- subprocess
- pyproject.toml