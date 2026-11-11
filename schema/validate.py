#!/usr/bin/env python3
"""Comprueba que el esquema o2.finding acepta los ejemplos válidos y rechaza los inválidos.

Uso: python3 schema/validate.py
Sale con código 0 si todo es correcto y 1 si algún ejemplo no se comporta como se espera.
"""

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = SCHEMA_DIR / "o2-finding.v0.schema.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    schema = load(SCHEMA_FILE)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    failures = 0

    for path in sorted((SCHEMA_DIR / "examples" / "valid").glob("*.json")):
        errors = list(validator.iter_errors(load(path)))
        if errors:
            failures += 1
            print(f"FALLO  {path.name}: debería ser válido")
            for error in errors:
                print(f"       - {error.message}")
        else:
            print(f"OK     {path.name}: válido")

    for path in sorted((SCHEMA_DIR / "examples" / "invalid").glob("*.json")):
        errors = list(validator.iter_errors(load(path)))
        if errors:
            print(f"OK     {path.name}: rechazado ({errors[0].message})")
        else:
            failures += 1
            print(f"FALLO  {path.name}: debería ser rechazado")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
