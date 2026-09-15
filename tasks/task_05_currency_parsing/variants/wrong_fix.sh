#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

old = ".fillna(0)"
new = ".fillna(-1)"

if old not in code:
    raise SystemExit("target expression not found")

path.write_text(code.replace(old, new))
PY

python /app/pipeline.py