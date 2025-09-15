import duckdb

#The most purchased product based on the age category (<30 vs ≥30)
query = """
WITH age_grouped AS (
    SELECT 
        CASE WHEN c.Age < 30 THEN 'Under 30' ELSE '30 and above' END AS Age_Group,
        o.Item,
        COUNT(*) AS Purchases
    FROM 'Order.csv' o
    JOIN 'Customer.csv' c ON o.Customer_ID = c.Customer_ID
    GROUP BY Age_Group, o.Item
)
SELECT Age_Group, Item, Purchases
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Age_Group ORDER BY Purchases DESC) AS rn
    FROM age_grouped
) ranked
WHERE rn = 1;
"""
df = duckdb.sql(query).df()
df.to_csv("output_q4_most_purchased_prod_age.csv", index=False)