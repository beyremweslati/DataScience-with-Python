import pandas as pd
sales = pd.read_csv("sales.csv")


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))