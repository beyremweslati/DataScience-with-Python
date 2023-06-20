import pandas as pd
temperatures = pd.read_csv("temperatures.csv")
# Add a year column to temperatures
temperatures["date"] = pd.to_datetime(temperatures['date'])
temperatures["year"] = temperatures["date"].dt.year
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c",index = ["country","city"], columns = "year")


# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc["Egypt":"India"])
print("---------------------------------")
# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")])
print("---------------------------------")


# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"),"2005":"2010"])