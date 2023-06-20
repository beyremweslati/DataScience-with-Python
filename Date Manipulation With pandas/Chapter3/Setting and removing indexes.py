import pandas as pd
temperatures = pd.read_csv("temperatures.csv")


# Look at temperatures
print(temperatures.head())
print("--------------------------------")
# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind.head())
print("--------------------------------")


# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index().head())
print("--------------------------------")

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True).head())