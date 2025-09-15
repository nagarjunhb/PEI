import duckdb

#The country that had minimum transactions and sales amount
query = """
WITH country_sales AS (
    SELECT 
        c.Country,
        COUNT(DISTINCT o.Order_ID) AS Transaction_Count,
        SUM(o.Amount) AS Total_Sales
    FROM 'Order.csv' o
    JOIN 'Customer.csv' c ON o.Customer_ID = c.Customer_ID
    GROUP BY c.Country
)
SELECT *
FROM country_sales
WHERE Transaction_Count = (SELECT MIN(Transaction_Count) FROM country_sales)
   OR Total_Sales = (SELECT MIN(Total_Sales) FROM country_sales)
"""
df = duckdb.sql(query).df()
df.to_csv("output_q5_country_with_min_transactions.csv", index=False)