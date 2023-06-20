import pandas as pd
temperatures = pd.read_csv("temperatures.csv")

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
print("---------------------------------")

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())
print("---------------------------------")

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))
print("---------------------------------")

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending = [True, False]))

print("Second Challenge: ")
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()
# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])
print("---------------------------------")

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

print("---------------------------------")

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])
