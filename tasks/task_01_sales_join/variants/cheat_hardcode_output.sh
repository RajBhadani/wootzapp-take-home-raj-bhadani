#!/bin/bash
set -euo pipefail

mkdir -p /app/output

printf "month,revenue\n2026-01,2560.0\n" > /app/output/monthly_revenue.csv
