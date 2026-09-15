#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path
import re

path = Path("/app/pipeline.py")
code = path.read_text()

pattern = (
    r'frame\["amount"\]\s*=\s*'
    r'pd\.to_numeric\('
    r'\s*frame\["amount"\],\s*'
    r'errors="coerce",\s*'
    r'\)\.fillna\(0\)'
)

replacement = (
    'frame["amount"] = pd.to_numeric('
    'frame["amount"].astype(str)'
    '.str.replace("$", "", regex=False)'
    '.str.replace(",", "", regex=False), '
    'errors="raise")'
)

updated, count = re.subn(pattern, replacement, code)

if count != 1:
    raise SystemExit("target bug expression not found")

path.write_text(updated)
PY

python /app/pipeline.py