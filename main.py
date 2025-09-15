import pandas as pd

# Read Excel file
df = pd.read_excel("Customer.xls")

# Save as CSV
df.to_csv("Customer.csv", index=False)
