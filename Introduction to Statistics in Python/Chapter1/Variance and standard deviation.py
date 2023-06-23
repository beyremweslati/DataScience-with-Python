import numpy as np
import pandas as pd

food_consumption = pd.read_csv("food_consumption.csv")
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby("food_category")["co2_emission"].agg(["var","std"]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
# Show plot
plt.show()
