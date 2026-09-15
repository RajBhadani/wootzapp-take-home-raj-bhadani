# Task 5: Silent Currency Parsing Loss



Create a monthly collections report from the payments data.



The input file is /app/data/payments.csv with these columns:



- payment_id

- paid_on

- amount



The amount column contains plain numbers and currency-formatted values such as $100.00 and $1,200.50.



The current pipeline silently converts some valid currency values into missing values and then zero, which makes the monthly total incorrect.



Fix pipeline.py only.



Parse all valid currency amounts correctly.



Write the final result to:



/app/output/monthly_collections.csv



The output must contain exactly these columns:



month,collections



Do not modify the input data or the verifier.

