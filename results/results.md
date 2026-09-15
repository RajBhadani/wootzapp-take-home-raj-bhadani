# Evaluation Results

Each task is evaluated with private hidden data and a deterministic verifier.

| Task | Correct Fix | Do Nothing | Wrong Fix | Cheat |
|---|---:|---:|---:|---:|
| Task 1 - Sales Join | 1.0 | 0.0 | 0.0 | PENDING |
| Task 2 - Timezone Shift | 1.0 | 0.0 | PENDING | PENDING |
| Task 3 - Group Imputation | 1.0 | PENDING | PENDING | PENDING |
| Task 4 - Aggregation Grain | 1.0 | PENDING | PENDING | PENDING |
| Task 5 - Currency Parsing | 1.0 | PENDING | PENDING | PENDING |

## Evaluation command

```cmd
harbor run -p tasks/<task-folder> -a <agent> -m <model>

## Task 3 Evaluation Note

The Task 3 baseline intentionally contains the global-mean imputation bug.
The solution script contains the category-wise median fix.

The Oracle trial did not modify the artifact, while Codex and Aider trials
could not run because of unavailable provider/network dependencies.