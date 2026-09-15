# WootzApp Take-Home Task

This repository contains five Harbor-based broken data-pipeline evaluation tasks.

Each task contains a small pipeline with one intentional bug, messy input data, a correct solution, wrong-fix variant, cheat variant, and a private deterministic verifier.

## Tasks

1. Sales join mismatch
2. UTC timezone conversion
3. Group-aware missing-value imputation
4. Customer-month aggregation grain
5. Currency string parsing

## Requirements

- Python 3.11 or newer
- Docker Desktop in Linux container mode
- Harbor CLI 0.23.0 or newer

## Generate tasks

```cmd
python generator\generate_tasks.py --difficulty medium --output generated_tasks