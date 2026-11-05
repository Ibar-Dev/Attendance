# Attendance Management System
## Estado Actual del Proyecto

**Fecha:** Noviembre 2026  
**Versión objetivo:** MVP v1

---

# Resumen Ejecutivo

Actualmente se ha completado la fase de fundación técnica del proyecto.

La infraestructura base ya está validada y funcionando:

- FastAPI operativo.
- SQLModel integrado.
- SQLite operativo.
- Gestión de dependencias mediante uv.
- Verificación estática mediante Ty.
- Linter mediante Ruff.
- Proyecto ejecutable localmente.

En esta fase el desarrollo se ha realizado utilizando una entidad de prueba (`Usuario`) con el objetivo de validar la arquitectura antes de implementar el dominio definitivo (`Attendance`).

---

# Estado de Avance

| Área | Estado |
|--------|--------|
| Python 3.14 | ✅ |
| uv | ✅ |
| FastAPI | ✅ |
| SQLModel | ✅ |
| SQLite | ✅ |
| Modelo de prueba Usuario | ✅ |
| Servicios | ✅ |
| Routers | ✅ |
| Ruff | ✅ |
| Ty | ✅ |
| Attendance | ⏳ Pendiente |
| Loguru | ⏳ Pendiente |
| Pytest | ⏳ Pendiente |
| Coverage | ⏳ Pendiente |
| Pre-commit | ⏳ Pendiente |
| Health Check | ⏳ Pendiente |
| README definitivo | ⏳ Pendiente |

---

# Arquitectura Implementada

Actualmente el proyecto sigue una estructura sencilla:

```text
app/
├── models/
├── services/
├── router/
├── database.py
└── main.py
```

Se ha optado por esta estructura para mantener la simplicidad durante el MVP.

---

# Validaciones de Calidad

Estado actual:

```bash
uv run ruff check .
```

Resultado:

```text
All checks passed
```

---

```bash
uv run ty check
```

Resultado:

```text
All checks passed
```

---

# Decisiones de Alcance

## Geolocalización

Queda excluida temporalmente del MVP.

Motivo:

Actualmente se está llevando a cabo una revisión legal y de privacidad para determinar si los datos de ubicación pueden ser almacenados o procesados.

Por tanto quedan fuera del MVP:

- Ciudad
- Provincia
- País
- Latitud
- Longitud
- Geolocalización desde navegador
- Procesamiento de ubicación

La posible incorporación de esta funcionalidad se evaluará en una fase posterior.

---

## Operaciones soportadas

El MVP únicamente contempla:

- Crear asistencias.
- Consultar asistencias.
- Listar asistencias.
- Filtrar asistencias.

Quedan fuera del MVP:

- Actualización de asistencias.
- Eliminación de asistencias.

---

# Próximo Hito

## Implementación del dominio Attendance

Siguiente tarea prioritaria:

```text
app/models/attendance.py
```

Modelo previsto:

```text
Attendance
├── id
├── guid
├── full_name
├── ggid
├── event_type
└── registered_at
```

Donde:

- `guid` será generado automáticamente.
- `registered_at` será generado automáticamente.

---

# Roadmap Inmediato

## Fase 1

Implementar modelo:

```text
Attendance
```

---

## Fase 2

Implementar servicio:

```text
attendance_service.py
```

Funcionalidad inicial:

```python
crear_attendance()
```

---

## Fase 3

Implementar endpoint:

```http
POST /attendances
```

---

## Fase 4

Implementar consultas:

```http
GET /attendances

GET /attendances/{id}

GET /attendances?ggid=

GET /attendances?event_type=
```

---

## Fase 5

Implementar:

```http
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok"
}
```

---

## Fase 6

Calidad y validación:

- Pytest
- Coverage
- Pre-commit
- Loguru

---

# Objetivo para considerar el MVP completado

Funcionalmente:

- Registro de asistencias operativo.
- Consulta de asistencias operativa.
- Filtrado operativo.
- Persistencia SQLite validada.
- Health Check operativo.

Calidad:

- Ruff en verde.
- Ty en verde.
- Tests pasando.
- Cobertura objetivo ≥ 80%.
- Hooks de pre-commit operativos.

---

# Riesgos Identificados

## Geolocalización

Pendiente de validación legal.

No se desarrollará ninguna funcionalidad asociada hasta disponer de una decisión formal.

---

## Alcance

Evitar incorporar durante el MVP:

- Docker
- PostgreSQL
- Alembic
- JWT
- OAuth
- Azure AD
- Azure OpenAI
- RAG
- Redis
- Kafka
- Dashboard analítico

Estas funcionalidades pertenecen a fases posteriores del roadmap.

---

# Estado General

El proyecto dispone de una base técnica estable y validada.

La prioridad inmediata es abandonar el modelo de prueba `Usuario` e implementar el dominio de negocio definitivo `Attendance`, manteniendo la simplicidad y el alcance definido para el MVP.
