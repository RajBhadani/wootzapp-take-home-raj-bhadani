\# Design Write-up



\## Scoring



Each verifier compares the actual output table against a private expected table. A correct table receives 1.0. Any missing, extra, or incorrect value receives 0.0. The comparison is deterministic and uses a small numeric tolerance.



\## Cheat attempt



The tested cheat writes a hard-coded answer to the output file without fixing the pipeline. The verifier blocks this by transferring the agent's pipeline code into a separate verifier container and running it against private hidden data. The expected answer is not available to the agent.



\## Design choices



1\. Pandas was chosen for readable data transformations instead of writing a custom CSV parser.

2\. A separate verifier environment was chosen instead of a shared environment so the agent cannot read private grading data.

3\. Exact table comparison was chosen instead of checking only whether the program ran.



\## Memory versus reasoning



To test memorisation, regenerate hidden data with a new seed while preserving the same bug type. An agent that memorised visible rows or totals should fail on the new fixtures, while an agent that understood the transformation should continue to pass.



\## Task summaries



\### Task 1: Sales Join Mismatch



The pipeline joins prices only by product instead of store and product. It tests multi-column joins and duplicate-row reasoning.



\### Task 2: Timezone Revenue Shift



The pipeline groups UTC timestamps before converting them to Asia/Kolkata. It tests timezone-aware date handling.



\### Task 3: Grouped Imputation Drift



The pipeline fills missing discounts with a global mean instead of a category-level median. It tests group-aware missing-value handling.



\### Task 4: Incorrect Aggregation Grain



The pipeline aggregates by customer instead of customer and month. It tests grouping grain and report design.



\### Task 5: Currency Parsing Loss



The pipeline converts currency strings to missing values and then zero. It tests robust text-to-number conversion.



\## Limitations



The fixtures are compact and deterministic. A future version would add more seeded rows, more edge cases, and repeated trials across several agents and models.

