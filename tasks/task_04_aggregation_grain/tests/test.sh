#!/bin/bash
set -euo pipefail

rm -rf /app/data /app/output
mkdir -p /app/data

cp -a /tests/hidden_data/. /app/data/

python /app/pipeline.py
python /tests/grader.py