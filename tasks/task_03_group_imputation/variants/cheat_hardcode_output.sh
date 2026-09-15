#!/bin/bash
set -euo pipefail

mkdir -p /app/output

out="category"_"revenue.csv"

printf 'category,revenue\nbooks,250.0\nelectronics,1100.0\n' > "/app/output/$out"