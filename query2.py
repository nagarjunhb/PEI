import duckdb

#Total number of transactions, total quantity sold, and total amount spent for each customer, with product details
query = """
SELECT 
    c.Customer_ID,
    c.First || ' ' || c.Last AS Customer_Name,
    o.Item,
    COUNT(DISTINCT o.Order_ID) AS Total_Transactions,
    COUNT(o.Item) AS Quantity_Sold,
    SUM(o.Amount) AS Total_Spent
FROM 'Order.csv' o
JOIN 'Customer.csv' c ON o.Customer_ID = c.Customer_ID
GROUP BY c.Customer_ID, Customer_Name, o.Item
ORDER BY c.Customer_ID
"""
df = duckdb.sql(query).df()
df.to_csv("output_q2_spend_by_customer.csv", index=False)