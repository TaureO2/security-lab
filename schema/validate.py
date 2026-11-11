#!/usr/bin/env python3
"""Check that the o2.finding schema accepts the valid examples and rejects the invalid ones.

Usage: python3 schema/validate.py
Exits with code 0 if everything is correct and 1 if any example does not behave as expected.
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
            print(f"FAIL   {path.name}: should be valid")
            for error in errors:
                print(f"       - {error.message}")
        else:
            print(f"OK     {path.name}: valid")

    for path in sorted((SCHEMA_DIR / "examples" / "invalid").glob("*.json")):
        errors = list(validator.iter_errors(load(path)))
        if errors:
            print(f"OK     {path.name}: rejected ({errors[0].message})")
        else:
            failures += 1
            print(f"FAIL   {path.name}: should be rejected")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
