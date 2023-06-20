import pandas as pd


temperatures = pd.read_csv("temperatures.csv")
temperatures_ind = temperatures.set_index(["country","city"])
temperatures_srt = temperatures_ind.sort_index()


# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad")])
print("---------------------------------")

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])
print("---------------------------------")

# Subset in both directions at once
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"),"date":"avg_temp_c"])