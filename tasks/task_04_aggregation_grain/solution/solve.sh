#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

old = "frame.groupby(CUSTOMER_ID, as_index=False)"
new = 'frame.groupby([CUSTOMER_ID, "month"], as_index=False)'

if old not in code:
    raise SystemExit("target expression not found")

path.write_text(code.replace(old, new))
PY

python /app/pipeline.py