import pandas as pd
gdp = pd.read_csv("WorldBank_GDP.csv")
pop = pd.read_csv("WorldBank_POP.csv")


# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp,pop, on=["Year","Country Name"],
                            fill_method='ffill')

# Print ctry_date
print(ctry_date.head())

print("--------------------------------------------------")
# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp,pop,on=["Country Name","Year"],fill_method="ffill")

# Print date_ctry
print(date_ctry.head())