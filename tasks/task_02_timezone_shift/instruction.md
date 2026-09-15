# Task 2: Timezone Revenue Shift

Create a daily revenue report for the Asia/Kolkata business day.

The input file is `/app/data/events.csv` with these columns:

- `event_id`
- `occurred_at`
- `amount`

The timestamps are in UTC ISO-8601 format. The current pipeline assigns dates before converting UTC timestamps to Asia/Kolkata, so transactions near midnight are assigned to the wrong business day.

Fix `pipeline.py` only.

Write the final result to:

```text
/app/output/daily_revenue.csv

```

The output must contain exactly these columns:

```text
date,revenue
```

Do not modify the input data or the verifier.