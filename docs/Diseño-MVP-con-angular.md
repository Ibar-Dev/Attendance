# Attendance Management System

## 1. Objetivo

Desarrollar una aplicación web para registrar la asistencia de participantes a eventos presenciales mediante una interfaz web Angular y una API REST desarrollada con FastAPI.

El sistema permitirá:

- Registrar asistencias.
- Consultar asistencias registradas.
- Filtrar registros.
- Garantizar la trazabilidad mediante identificadores únicos.

---

## 2. Alcance del MVP

### Incluido

#### Backend

- FastAPI
- SQLModel
- SQLite
- Pydantic v2
- Loguru
- OpenAPI

#### Frontend

- Angular
- TypeScript
- HttpClient
- Formulario de registro de asistencia
- Listado de asistencias
- Consulta de estado de la API

#### Datos de asistencia

- Nombre completo
- GGID
- Convocatoria
- Fecha de registro
- GUID

#### Funcionalidades

- Crear asistencia
- Obtener asistencia
- Listar asistencias
- Filtrar asistencias por GGID
- Filtrar asistencias por convocatoria
- Health Check

#### Calidad

- Pytest
- Ruff
- Ty
- Coverage
- Pre-commit

---

### No incluido (MVP v1)

#### Seguridad

- JWT
- OAuth
- Azure AD
- Roles
- Login

#### Infraestructura

- Docker
- PostgreSQL
- Alembic
- CI/CD
- Configuración multi-entorno

#### Frontend avanzado

- Angular Material
- NgRx
- SSR
- PWA
- Internacionalización

#### Geolocalización

- Ciudad
- Provincia
- País
- Latitud
- Longitud

#### IA y Analítica

- Azure OpenAI
- RAG
- Dashboard
- Exportación avanzada

---

## 3. Arquitectura

┌──────────────┐
│ Angular │
└──────┬───────┘
│ HTTP
▼
┌──────────────┐
│ FastAPI │
├──────────────┤
│ Endpoints │
│ Validaciones │
│ Servicios │
│ Logging │
└──────┬───────┘
│
▼
┌──────────────┐
│ SQLModel │
└──────┬───────┘
│
▼
┌──────────────┐
│ SQLite │
└──────────────┘

---

## 4. Stack Tecnológico

### Backend

- Python 3.14
- FastAPI
- SQLModel
- SQLite
- Pydantic v2
- Loguru

### Frontend

- Angular
- TypeScript
- Angular CLI
- HttpClient

### Calidad

- Pytest
- Ruff
- Ruff Format
- Ty
- Coverage
- Pre-commit

---

## 7. Estructura del Proyecto

attendance/

├── backend/

│ ├── app/

│ ├── tests/

│ └── pyproject.toml

│

├── frontend/

│ ├── src/

│ ├── angular.json

│ └── package.json

│

└── docs/

---

## 9. Roadmap Técnico

### Fase 1 - MVP

Backend:

- Attendance
- FastAPI
- SQLModel
- SQLite

Frontend:

- Angular
- Formulario asistencia
- Listado asistencias
- Health Check

Calidad:

- Ruff
- Ty
- Pytest
- Coverage
- Pre-commit

### Fase 2

- PostgreSQL
- Docker
- Alembic
- Variables entorno

### Fase 3

- JWT
- Azure AD
- Roles

### Fase 4

- Azure OpenAI
- Dashboard
- Analítica