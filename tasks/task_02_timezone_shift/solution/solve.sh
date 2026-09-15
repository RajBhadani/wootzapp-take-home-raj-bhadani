#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

old = "frame[OCCURRED_AT].dt.date"
new = 'frame[OCCURRED_AT].dt.tz_convert("Asia/Kolkata").dt.date'

if old not in code:
    raise SystemExit("target bug expression not found")

path.write_text(code.replace(old, new))
PY

python /app/pipeline.py