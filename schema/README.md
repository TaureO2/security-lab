# Esquema común `o2.finding`

Formato JSON que usan todas las herramientas del ecosistema para describir un hallazgo de seguridad. Así, lo que produce una herramienta lo puede leer otra, un SIEM o un informe.

Versión actual: **v0** ([`o2-finding.v0.schema.json`](o2-finding.v0.schema.json)), en formato JSON Schema 2020-12.

## Campos

| Campo | Obligatorio | Descripción |
| --- | --- | --- |
| `schema` | Sí | Siempre `"o2.finding/v0"` |
| `tool` | Sí | Herramienta que genera el hallazgo, en minúsculas (`authwatch`) |
| `timestamp` | Sí | Momento del evento, en RFC 3339 (`2026-11-20T10:42:13Z`) |
| `severity` | Sí | `info`, `low`, `medium`, `high` o `critical` |
| `title` | Sí | Resumen legible, hasta 200 caracteres |
| `id` | No | Identificador del hallazgo dentro de la ejecución |
| `tool_version` | No | Versión de la herramienta (semver) |
| `host` | No | Equipo donde ocurrió el evento |
| `attack` | No | Técnicas de MITRE ATT&CK (`T1110`, `T1110.001`) |
| `evidence` | No | Datos que justifican el hallazgo; libre para cada herramienta |
| `recommendation` | No | Acción sugerida para el analista |

No se admiten campos fuera de esta lista. Lo específico de cada herramienta va dentro de `evidence`.

## Ejemplo

```json
{
  "schema": "o2.finding/v0",
  "tool": "authwatch",
  "timestamp": "2026-11-20T10:42:13Z",
  "host": "hosp-lnx-01",
  "severity": "high",
  "title": "Posible fuerza bruta SSH",
  "attack": ["T1110.001"],
  "evidence": { "source_ip": "203.0.113.45", "failures": 37, "window_minutes": 5 },
  "recommendation": "Bloquear la IP y revisar si hubo un acceso correcto posterior desde ella."
}
```

Más ejemplos en [`examples/valid/`](examples/valid/). En [`examples/invalid/`](examples/invalid/) hay casos que el esquema debe rechazar.

## Validación

```bash
pip install jsonschema
python3 schema/validate.py
```

La validación se ejecuta también en GitHub Actions con cada cambio.

## Versionado

Una versión publicada no cambia. Si hace falta un cambio incompatible (quitar un campo, cambiar un tipo), se crea `v1` en un archivo nuevo y las herramientas migran a su ritmo.
