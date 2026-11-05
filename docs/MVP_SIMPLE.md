# Diseño Técnico MVP

# Attendance Management System

## 1. Objetivo

Desarrollar una aplicación web para registrar la asistencia de participantes a eventos presenciales mediante una interfaz sencilla y una API REST.

El sistema permitirá:

- Registrar asistencias.
- Consultar asistencias registradas.
- Filtrar registros.
- Garantizar la trazabilidad de cada registro mediante identificadores únicos.

> Este documento define exclusivamente los aspectos técnicos del MVP y excluye requisitos legales, auditorías corporativas, protección de datos y aspectos regulatorios.

---

## 2. Alcance del MVP

### Incluido

#### Backend

- API REST con FastAPI.
- Persistencia mediante SQLModel.
- Base de datos SQLite.
- Validación de datos con Pydantic v2.
- Logging estructurado básico mediante Loguru.
- Documentación OpenAPI automática.

#### Datos de asistencia

- Nombre completo.
- GGID.
- Convocatoria.
- Fecha de registro.
- GUID.

#### Funcionalidades

- Crear asistencia.
- Obtener una asistencia.
- Listar asistencias.
- Filtrar asistencias por GGID.
- Filtrar asistencias por convocatoria.
- Health Check.

#### Calidad

- Testing automatizado.
- Linter.
- Formateador.
- Verificación de tipos.
- Automatización de validaciones mediante pre-commit.

---

### No incluido (MVP v1)

#### Seguridad y autenticación

- Login.
- Roles.
- Azure AD.
- OAuth.
- JWT.

#### Infraestructura

- Docker.
- PostgreSQL.
- Alembic.
- CI/CD.
- Configuración multi-entorno.

#### Frontend

- Frontend React.

#### Geolocalización

- Ciudad.
- Provincia.
- País.
- Latitud.
- Longitud.
- Geolocalización real desde navegador.
- Almacenamiento de datos de localización.
- Cualquier procesamiento o explotación de datos geográficos.

#### IA y analítica

- Azure OpenAI.
- RAG.
- Dashboard analítico.
- Detección automática de patrones.
- Exportación avanzada de informes.

#### Observabilidad avanzada

- OpenTelemetry.
- Grafana.
- ELK.
- Loki.

#### Componentes distribuidos

- Redis.
- Kafka.
- Kubernetes.

#### Gestión de registros

- Modificación de asistencias (PUT/PATCH).
- Eliminación de asistencias (DELETE).

---

## 3. Arquitectura

```text
┌─────────────────┐
│     Cliente     │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐
│     FastAPI     │
├─────────────────┤
│ Endpoints       │
│ Validaciones    │
│ Casos de uso    │
│ Logging         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    SQLModel     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     SQLite      │
└─────────────────┘
```

---

## 4. Stack Tecnológico

### Backend

| Tecnología | Motivo |
|------------|---------|
| Python 3.14 | Lenguaje principal |
| FastAPI | API moderna y tipada |
| SQLModel | ORM basado en SQLAlchemy |
| Pydantic v2 | Validación y serialización |
| Uvicorn | Servidor ASGI |
| Loguru | Logging estructurado básico |

### Gestión del Proyecto

| Herramienta | Uso |
|-------------|-----|
| uv | Gestión de dependencias, entornos virtuales y ejecución |
| Git | Control de versiones |

### Base de Datos

| Etapa | Tecnología |
|--------|------------|
| MVP | SQLite |
| Futuro | PostgreSQL |

La aplicación debe diseñarse para que la migración a PostgreSQL requiera únicamente cambios de configuración y de cadena de conexión.

### Calidad

| Herramienta | Uso |
|-------------|-----|
| Pytest | Testing automatizado |
| Ruff | Linter |
| Ruff Format | Formateo de código |
| Ty | Verificación de tipos |
| Coverage | Métrica orientativa |
| Pre-commit | Automatización de validaciones |

### Observabilidad

| Herramienta | Uso |
|-------------|-----|
| Loguru | Logging estructurado |
| Health Check Endpoint | Monitorización básica de la API |

---

## 5. Modelo de Dominio

### Attendance

| Campo | Tipo |
|---------|------|
| id | int |
| guid | UUID |
| full_name | str |
| ggid | str |
| event_type | str |
| registered_at | datetime |

### Consideraciones

- `id` es la clave primaria interna.
- `guid` es generado automáticamente por el sistema.
- `registered_at` es generado automáticamente por el sistema.
- `ggid` permite realizar búsquedas y filtrados.
- No se almacenará información de geolocalización durante el MVP.

---

## 6. Endpoints MVP

### Crear asistencia

```http
POST /attendances
```

### Obtener asistencia

```http
GET /attendances/{id}
```

### Listar asistencias

```http
GET /attendances
```

### Filtrar por GGID

```http
GET /attendances?ggid=123456
```

### Filtrar por convocatoria

```http
GET /attendances?event_type=lunes
```

### Health Check

```http
GET /health
```

Respuesta:

```json
{
  "status": "ok"
}
```

---

## 7. Estructura de Proyecto

```text
attendance/
│
├── app/
│   │
│   ├── api/
│   │   └── attendances.py
│   │
│   ├── models/
│   │   └── attendance.py
│   │
│   ├── services/
│   │   └── attendance_service.py
│   │
│   ├── database.py
│   │
│   ├── core/
│   │   └── logging.py
│   │
│   └── main.py
│
├── tests/
│
├── pyproject.toml
├── uv.lock
├── README.md
│
└── attendance.db
```

> Durante el MVP se prioriza la simplicidad. Se evitarán capas adicionales que no aporten valor directo al alcance definido.

---

## 8. Criterios de Éxito del MVP

El MVP se considera completado cuando:

### Funcionalidad

- Se puede registrar una asistencia.
- Se puede consultar una asistencia.
- Se pueden listar asistencias.
- Se pueden filtrar asistencias por GGID.
- Se pueden filtrar asistencias por convocatoria.
- Los datos persisten tras reiniciar la aplicación.
- El endpoint de Health Check responde correctamente.

### Calidad

- Todos los endpoints del MVP disponen de tests automatizados.
- Objetivo orientativo de cobertura: ≥ 80%.
- Sin errores de Ruff.
- Sin errores reportados por Ty.
- Todos los tests pasan correctamente.
- Los hooks de pre-commit se ejecutan sin errores.

### Rendimiento

- La aplicación responde de forma fluida en entorno local para el volumen esperado durante el MVP.
- El sistema mantiene tiempos de respuesta adecuados para consultas y registros básicos.

---

## 9. Roadmap Técnico

### Fase 1 - MVP

- FastAPI
- SQLModel
- SQLite
- Gestión básica de asistencias
- Logging con Loguru
- Pytest
- Ruff
- Ty
- uv
- OpenAPI

### Fase 2

- PostgreSQL
- Alembic
- Docker
- Variables de entorno
- Configuración por entornos

### Fase 3

- Autenticación JWT
- Roles y permisos
- Azure AD
- Gestión de usuarios

### Fase 4

- Azure OpenAI
- Extracción inteligente de métricas
- Detección de patrones de asistencia
- Dashboard analítico
- Exportación de informes

---

## 10. Principios de Diseño

Durante el MVP se priorizarán los siguientes principios:

- Simplicidad sobre sobreingeniería.
- Arquitectura evolutiva.
- Tipado estático en todo el código.
- Separación clara de responsabilidades.
- Trazabilidad mediante GUID.
- Compatibilidad futura con PostgreSQL.
- Código orientado a mantenibilidad y testing.
- Desarrollo incremental basado en funcionalidades completas.

---

## Decisiones de Alcance

### Geolocalización

Toda funcionalidad relacionada con ubicación queda fuera del MVP hasta finalizar la evaluación legal correspondiente.

### Operaciones soportadas

El MVP contempla únicamente:

- Creación de asistencias.
- Consulta individual de asistencias.
- Consulta de listados.
- Filtrado de resultados.

Las operaciones de actualización y eliminación se evaluarán en futuras iteraciones en función de las necesidades del negocio.

### Filosofía del MVP

El objetivo principal es disponer de una solución funcional, mantenible y validada técnicamente antes de introducir complejidad adicional relacionada con seguridad avanzada, infraestructura, analítica o inteligencia artificial.