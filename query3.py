import duckdb

#The maximum product purchased for each country (by spend)
query = """
WITH product_sales AS (
    SELECT 
        c.Country,
        o.Item,
        SUM(o.Amount) AS Total_Spent
    FROM 'Order.csv' o
    JOIN 'Customer.csv' c ON o.Customer_ID = c.Customer_ID
    GROUP BY c.Country, o.Item
)
SELECT Country, Item, Total_Spent
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Country ORDER BY Total_Spent DESC) AS rn
    FROM product_sales
) ranked
WHERE rn = 1
"""
df = duckdb.sql(query).df()
df.to_csv("output_q3_max_product_per_country.csv", index=False)