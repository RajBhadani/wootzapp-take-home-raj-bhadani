# WootzApp Take-Home Task - Progress

## Current status

Task 1 is implemented as the first Harbor task. The remaining four tasks, the shared generator, final results table, README, and one-page write-up are still pending.

## Completed

- Created the GitHub repository and baseline project folders.
- Installed and verified Docker Desktop in Linux container mode.
- Installed the Harbor CLI (`harbor 0.23.0`).
- Created Task 1: **Sales Join Mismatch**.
  - Messy sales and store-specific product-price input data.
  - Buggy Python/pandas revenue pipeline.
  - Harbor task configuration and Docker environment.
  - Oracle solution, wrong-fix variant, and hard-coded-output cheat variant.
  - Deterministic verifier and separate verifier Docker environment.
- Added a five-task design plan in `docs/task_designs.md`.
- Added `.gitattributes` so shell scripts use Linux LF line endings.

## Task 1 results recorded so far

| Variant | Reward | Result |
|---|---:|---|
| Correct fix / Oracle | 1.0 | Passed |
| Do nothing / `nop` agent | 0.0 | Passed expected negative test |
| Wrong fix | 0.0 | Passed expected negative test |

## Task 1 hardening in progress

The first checker compared against a known output, so a hard-coded CSV could potentially pass. The verifier has been updated in GitHub to:

- receive the agent's `pipeline.py` as an artifact;
- run that pipeline against private February test data;
- score the hidden expected revenue of `1115.0`.

This hardened configuration still needs to be pulled locally and verified with all four variants: correct fix, do nothing, wrong fix, and cheat.

## Remaining work

1. Verify the hardened Task 1 checker and save its real logs/results.
2. Build `generator/generate_tasks.py` with `easy`, `medium`, and `hard` modes.
3. Generate four additional tasks with unique bugs:
   - timezone conversion;
   - group-wise missing-value imputation;
   - incorrect aggregation grain;
   - currency/text numeric parsing.
4. Create an oracle solution, wrong fix, cheat test, and deterministic hidden verifier for every task.
5. Run the complete correct/do-nothing/wrong-fix matrix and save the real score table.
6. Write the one-page submission write-up.
7. Complete the README with setup, generation, evaluation, results, and limitations.
8. Perform a clean-clone reproducibility test before submission.

## Important implementation rule

Correct answers and verifier expectations must not be exposed to the agent during a Harbor run. Separate verifier environments and hidden test data are used to enforce this.
