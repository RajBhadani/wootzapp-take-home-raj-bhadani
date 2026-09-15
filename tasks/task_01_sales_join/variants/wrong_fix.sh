#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

path.write_text(code.replace('how="left"', 'how="inner"'))
PY

python /app/pipeline.py
