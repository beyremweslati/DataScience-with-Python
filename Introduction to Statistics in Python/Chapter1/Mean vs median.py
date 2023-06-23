import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

food_consumption = pd.read_csv("food_consumption.csv")
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption["food_category"] == "rice"]

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption["co2_emission"].agg(["mean","median"]))

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption["co2_emission"])
plt.show()
