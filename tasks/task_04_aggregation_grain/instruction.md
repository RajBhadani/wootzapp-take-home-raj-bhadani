# Task 4: Incorrect Aggregation Grain



Create a revenue report for every customer and calendar month.



The input file is /app/data/invoices.csv with these columns:



- invoice_id

- customer_id

- invoice_date

- amount



The current pipeline combines multiple months for the same customer into one row, so the report uses the wrong aggregation grain.



Fix pipeline.py only.



The output must contain one row for every customer-month combination.



Write the final result to:



/app/output/customer_month_revenue.csv



The output must contain exactly these columns:



customer_id,month,revenue



Do not modify the input data or the verifier.

