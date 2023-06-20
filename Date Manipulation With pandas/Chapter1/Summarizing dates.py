import pandas as pd
sales = pd.read_csv("sales.csv")

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())