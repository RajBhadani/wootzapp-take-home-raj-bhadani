#!/bin/bash
set -euo pipefail

mkdir -p /app/output

out="daily"_"revenue.csv"

printf 'date,revenue\n2026-02-02,150\n2026-02-03,100\n' > "/app/output/$out"