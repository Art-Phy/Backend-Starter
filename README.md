### Backend Starter

Backend Starter es una herramienta CLI desarrollada en Python para generar de forma automática la estructura inicial de un proyecto backend.

El objetivo es evitar repetir manualmente la creación de carpetas y archivos comunes cada vez que se inicia un nuevo proyecto.

#### Funcionalidades

- Creación automática de un nuevo proyecto.
- Generación de archivos base:
  - README.md
  - CHANGELOG.md
  - requirements.txt
  - .gitignore
- Creación de estructura `src/`.
- Creación de paquete Python inicial.
- Creación de carpeta `tests/`.
- Preparado para evolucionar hacia automatización con Git, entornos virtuales y plantillas.

#### Estructura generada

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

#### Uso Actual
Desde la raíz del proyecto
```
PYTHONPATH=src python3 -m backend_starter.cli my_project
```

#### Objetivo del proyecto
Este proyecto nace como una herramienta práctica para automatizar el arranque de proyectos backend en Python.

Está pensado para crecer progresivamente con nuevas funcionalidades como:

* Inicialización automática de Git.
* Creación de rama develop.
* Creación opcional de entorno virtual.
* Plantillas para proyectos CLI.
* Plantillas para proyectos FastAPI.
* Instalación como comando global.

#### Tecnologías
* Python 3
* pathlib
* CLI básica con sys.argv
