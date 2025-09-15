import duckdb

#Total amount spent and the country for the Pending delivery status for each country
query = """
SELECT c.Country, SUM(o.Amount) AS Total_Pending
FROM 'Order.csv' o
JOIN 'Customer.csv' c ON o.Customer_ID = c.Customer_ID
JOIN 'Shipping.json' s ON c.Customer_ID = s.Customer_ID
WHERE s.Status = 'Pending'
GROUP BY c.Country
"""
df = duckdb.sql(query).df()
df.to_csv("output_q1_pending_spend.csv", index=False)
