# Common schema `o2.finding`

The JSON format that all the tools in the ecosystem use to describe a security finding. This way, what one tool produces can be read by another tool, a SIEM or a report.

Current version: **v0** ([`o2-finding.v0.schema.json`](o2-finding.v0.schema.json)), in JSON Schema 2020-12 format.

## Fields

| Field | Required | Description |
| --- | --- | --- |
| `schema` | Yes | Always `"o2.finding/v0"` |
| `tool` | Yes | Tool that creates the finding, in lower case (`authwatch`) |
| `timestamp` | Yes | Time of the event, in RFC 3339 (`2026-11-20T10:42:13Z`) |
| `severity` | Yes | `info`, `low`, `medium`, `high` or `critical` |
| `title` | Yes | Short readable summary, up to 200 characters |
| `id` | No | Identifier of the finding within one run of the tool |
| `tool_version` | No | Version of the tool (semver) |
| `host` | No | Machine where the event happened |
| `attack` | No | MITRE ATT&CK techniques (`T1110`, `T1110.001`) |
| `evidence` | No | Data that supports the finding; free for each tool |
| `recommendation` | No | Suggested action for the analyst |

Fields that are not in this list are not allowed. Tool-specific data goes inside `evidence`.

## Example

```json
{
  "schema": "o2.finding/v0",
  "tool": "authwatch",
  "timestamp": "2026-11-20T10:42:13Z",
  "host": "hosp-lnx-01",
  "severity": "high",
  "title": "Possible SSH brute force",
  "attack": ["T1110.001"],
  "evidence": { "source_ip": "203.0.113.45", "failures": 37, "window_minutes": 5 },
  "recommendation": "Block the IP address and check whether there was a successful login from it later."
}
```

More examples in [`examples/valid/`](examples/valid/). [`examples/invalid/`](examples/invalid/) has cases that the schema must reject.

## Validation

```bash
pip install jsonschema
python3 schema/validate.py
```

The validation also runs on GitHub Actions with every change.

## Versions

A published version does not change its rules. If an incompatible change is needed (removing a field, changing a type), a `v1` is created in a new file and the tools move to it at their own pace.
