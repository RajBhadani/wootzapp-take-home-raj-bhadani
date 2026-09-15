#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

old = 'on="product_id",'
new = 'on=["store_id", "product_id"],'

if old not in code:
    raise RuntimeError("Expected join statement was not found.")

path.write_text(code.replace(old, new))
PY

python /app/pipeline.py
