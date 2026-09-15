#!/bin/bash
set -euo pipefail

rm -rf /app/output

python /app/pipeline.py
python /tests/grader.py
