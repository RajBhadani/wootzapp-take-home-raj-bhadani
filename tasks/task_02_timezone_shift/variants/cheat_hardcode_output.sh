#!/bin/bash
set -euo pipefail

mkdir -p /app/output

out="daily"_"revenue.csv"

{
    echo "date,revenue"
    echo "2026-02-02,150"
    echo "2026-02-03,100"
} > "/app/output/$out"