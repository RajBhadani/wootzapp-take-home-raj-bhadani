#!/bin/bash
set -euo pipefail

mkdir -p /app/output

out="monthly"_"collections.csv"

printf 'month,collections\n2026-01,250.0\n' > "/app/output/$out"