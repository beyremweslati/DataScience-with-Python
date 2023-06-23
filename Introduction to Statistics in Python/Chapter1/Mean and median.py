# Import numpy with alias np
import numpy as np
import pandas as pd

food_consumption = pd.read_csv("food_consumption.csv")
# Filter for Belgium
be_consumption = food_consumption[food_consumption["country"] == "Belgium"]

# Filter for USA
usa_consumption = food_consumption[food_consumption["country"] == "USA"]

# Calculate mean and median consumption in Belgium
print(be_consumption["consumption"].mean())
print(be_consumption["consumption"].median())

# Calculate mean and median consumption in USA
print(usa_consumption["consumption"].mean())
print(usa_consumption["consumption"].median())


print("-----------------------------")

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption["country"]=="Belgium") | (food_consumption["country"]=="USA")]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby("country")["consumption"].agg(["mean","median"]))