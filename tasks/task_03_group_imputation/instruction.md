# Task 3: Grouped Imputation Drift



Create a category revenue report from the orders data.



The input file is `/app/data/orders.csv` with these columns:



- `order_id`

- `category`

- `list_price`

- `discount`



Some discount values are missing. The current pipeline fills missing discounts using one global value, which makes category revenue incorrect.



Fix `pipeline.py` only.



Missing discounts must be filled using the typical discount for the same category.



Write the final result to:



/app/output/category_revenue.csv



The output must contain exactly these columns:



category,revenue



Do not modify the input data or the verifier.

