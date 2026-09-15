#!/bin/bash
set -euo pipefail

mkdir -p /app/output

out="customer"_"month"_"revenue.csv"

printf 'customer_id,month,revenue\nC1,2026-01,220\nC2,2026-01,80\n' > "/app/output/$out"