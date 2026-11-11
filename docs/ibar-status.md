# Attendance Management System

## Estado Actual del Proyecto

Fecha: Noviembre 2026

Versión objetivo: MVP v1

---

# Resumen Ejecutivo

Actualmente se ha completado la fundación técnica del backend.

La infraestructura base ya está validada:

- FastAPI operativo
- SQLModel operativo
- SQLite operativo
- uv configurado
- Ruff operativo
- Ty operativo
- Proyecto ejecutable localmente

Adicionalmente se ha decidido incorporar Angular como frontend oficial del MVP.

---

# Estado de Avance

| Área | Estado |
|--------|--------|
| Python 3.14 | ✅ |
| uv | ✅ |
| FastAPI | ✅ |
| SQLModel | ✅ |
| SQLite | ✅ |
| Modelo Usuario | ✅ |
| Servicios Usuario | ✅ |
| Routers Usuario | ✅ |
| Ruff | ✅ |
| Ty | ✅ |
| Angular Workspace | ⏳ |
| Attendance | ⏳ |
| Health Check | ⏳ |
| Loguru | ⏳ |
| Pytest | ⏳ |
| Coverage | ⏳ |
| Pre-commit | ⏳ |

---

# Arquitectura Implementada

app/

├── models/

├── services/

├── router/

├── database.py

└── main.py

---

# Arquitectura Objetivo

backend/

├── app/

├── tests/

└── pyproject.toml

frontend/

├── src/

├── angular.json

└── package.json

---

# Próximo Hito

Implementar el dominio de negocio:

app/models/attendance.py

---

# Roadmap Inmediato

## Backend

1. Attendance model
2. Attendance service
3. POST /attendances
4. GET /attendances
5. GET /attendances/{id}
6. Filtros
7. Health Check

## Frontend

1. Crear proyecto Angular
2. Configurar HttpClient
3. Crear AttendanceService
4. Crear formulario
5. Crear listado
6. Conectar con API

---

# Objetivo MVP

Backend:

- Registro operativo
- Consulta operativa
- Filtros operativos
- SQLite persistente
- Health Check

Frontend:

- Crear asistencia
- Listar asistencias
- Consumir API FastAPI

Calidad:

- Ruff verde
- Ty verde
- Tests OK
- Coverage >= 80%
- Pre-commit OK

---

# Estado General

El backend dispone de una base estable validada.

La prioridad inmediata es:

1. Sustituir Usuario por Attendance.
2. Implementar endpoints del MVP.
3. Crear frontend Angular mínimo.
4. Incorporar testing.
