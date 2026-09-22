
<p align="left">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Project%20Generator-orange" />
  <img src="https://img.shields.io/badge/GitFlow-Automated-green" />
  <img src="https://img.shields.io/badge/VirtualEnv-Optional-success" />
  <img src="https://img.shields.io/badge/Installable-CLI-success" />
  <img src="https://img.shields.io/badge/AI%20Templates-Optional-blueviolet" />
  <img src="https://img.shields.io/badge/FastAPI-Template-009688" />
  <img src="https://img.shields.io/badge/Tests-4%20Passing-success" />
  <img src="https://img.shields.io/badge/Version-v0.9.0-success" />
</p>


### Backend Starter

Backend Starter es una herramienta CLI desarrollada en Python para generar automáticamente la estructura inicial de proyectos backend.

El objetivo es evitar repetir manualmente la creación de carpetas, archivos, repositorios Git y configuraciones comunes cada vez que se inicia un nuevo proyecto.

El sistema utiliza una arquitectura modular de plantillas que permite generar distintos tipos de proyecto manteniendo un flujo de creación común.


#### Funcionalidades

- Creación automática de nuevos proyectos Python.
- Sistema modular de plantillas mediante `--template`.
- Plantilla `basic` para proyectos Python generales.
- Plantilla `fastapi` funcional para APIs backend.
- Generación de archivos base:
  - `README.md`
  - `CHANGELOG.md`
  - `requirements.txt`
  - `.gitignore`
- Creación de estructura `src/`.
- Creación del paquete Python inicial.
- Creación de carpeta `tests/`.
- Inicialización automática de repositorio **Git**.
- Creación automática de rama **develop**.
- Creación opcional de entorno virtual mediante `--venv`.
- Generación opcional de `AGENT.md` y `PROJECT.md` mediante `--ai`.
- Ayuda integrada mediante `argparse`.
- Instalación como herramienta CLI mediante `pip`.
- Compatible con instalación mediante `pipx`.
- Tests automatizados mediante `pytest`.


#### Plantillas disponibles

##### Basic

Genera una estructura Python mínima preparada para comenzar el desarrollo.

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

Uso:

```bash
backend-starter my_project
```

También puede seleccionarse explícitamente:

```bash
backend-starter my_project --template basic
```


##### FastAPI

Genera una API mínima y funcional utilizando FastAPI.

```text
my_api/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── src/
│   └── my_api/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── __init__.py
```

La plantilla incluye:

- Aplicación FastAPI funcional.
- Endpoint inicial `GET /`.
- `requirements.txt` con:
  - `fastapi`
  - `uvicorn[standard]`
- README específico con instrucciones de instalación y ejecución.
- Acceso automático a la documentación Swagger mediante `/docs`.

Uso:

```bash
backend-starter my_api --template fastapi
```

Con entorno virtual y documentación para IA:

```bash
backend-starter my_api --template fastapi --venv --ai
```

Una vez instaladas las dependencias, la aplicación generada puede ejecutarse con:

```bash
uvicorn my_api.main:app --app-dir src --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```


#### Documentación opcional para IA

Mediante la opción:

```bash
--ai
```

Backend Starter añade:

```text
AGENT.md
PROJECT.md
```

Estos archivos proporcionan una base para documentar el contexto del proyecto y las instrucciones destinadas a asistentes o agentes de IA.

Ejemplo:

```bash
backend-starter my_project --ai
```


#### Entorno virtual opcional

Backend Starter puede crear automáticamente un entorno virtual dentro del proyecto:

```bash
backend-starter my_project --venv
```

Esto genera:

```text
.venv/
```

Las distintas opciones pueden combinarse:

```bash
backend-starter my_api --template fastapi --venv --ai
```


#### Instalación

##### Desarrollo

```bash
git clone https://github.com/Art-Phy/backend-starter.git
cd backend-starter

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e .
```

##### Uso recomendado

Backend Starter puede instalarse de forma aislada mediante `pipx`:

```bash
brew install pipx
pipx ensurepath

pipx install git+https://github.com/Art-Phy/backend-starter.git
```

Después de la instalación:

```bash
backend-starter --help
```

#### Uso

Proyecto básico:

```bash
backend-starter my_project
```

Seleccionando una plantilla:

```bash
backend-starter my_project --template fastapi
```

Con entorno virtual:

```bash
backend-starter my_project --venv
```

Con documentación para IA:

```bash
backend-starter my_project --ai
```

Combinando opciones:

```bash
backend-starter my_project --template fastapi --venv --ai
```

#### Testing

Instala las dependencias necesarias para desarrollo y ejecuta:

```bash
pytest
```

Actualmente, la suite valida el comportamiento principal de la plantilla FastAPI, incluyendo:

- Generación de `main.py`.
- Dependencias necesarias para FastAPI.
- Generación de una aplicación FastAPI válida.
- Uso correcto del nombre importable del paquete en las instrucciones de ejecución.

#### Objetivo del proyecto

Backend Starter nace como una herramienta para automatizar el arranque de proyectos backend en Python.

La arquitectura modular de plantillas permite ampliar progresivamente la herramienta sin acoplar nuevos tipos de proyecto al generador principal.

Próximas líneas de evolución:

- Plantilla funcional para proyectos CLI.
- Evolución de las plantillas backend.
- Integración con Docker.
- Integración con GitHub Actions.
- Ampliación de la suite de tests.

#### Tecnologías

- Python 3
- FastAPI
- pytest
- pathlib
- argparse
- subprocess
- pyproject.toml
- Git
