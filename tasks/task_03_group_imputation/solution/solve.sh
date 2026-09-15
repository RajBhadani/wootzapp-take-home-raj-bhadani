#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/pipeline.py")
code = path.read_text()

old = '''frame["discount"] = frame["discount"].fillna(
    frame["discount"].mean()
)'''

new = '''category_medians = frame.groupby("category")["discount"].transform("median")
frame["discount"] = frame["discount"].fillna(category_medians)'''

if old not in code:
    raise SystemExit("target bug expression not found")

path.write_text(code.replace(old, new))
PY

python /app/pipeline.py