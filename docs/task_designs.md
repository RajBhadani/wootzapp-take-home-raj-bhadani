# Task Designs

| Task | Name | Hidden bug | Skill tested |
|---|---|---|---|
| 1 | Sales Join Mismatch | Join only uses `product_id` instead of `store_id` and `product_id`. | Multi-column joins and duplicate-row diagnosis |
| 2 | Timezone Revenue Shift | Timestamps are parsed without correctly converting timezones before daily aggregation. | Date/time parsing and timezone handling |
| 3 | Grouped Imputation Drift | Missing values are filled using a global average instead of a category-level value. | Missing-data handling |
| 4 | Incorrect Aggregation Level | Revenue is aggregated by customer instead of customer and month. | Grouping and aggregation logic |
| 5 | Silent Currency Parsing Loss | Currency strings with commas/symbols are silently converted to missing values. | Data cleaning and numeric conversion |

## Difficulty levels

- Easy: Few rows, clear column names, and one obvious edge case.
- Medium: More rows, mixed formats, and distractor columns.
- Hard: Rare edge cases, ambiguous column names, and larger datasets.
