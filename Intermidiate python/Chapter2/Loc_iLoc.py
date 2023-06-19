# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Print out observation for Japan
print(cars.loc["JPN"])
# Print out observations for Australia and Egypt
print(cars.loc[["AUS","EG"]])


#--------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc["MOR","drives_right"])

# Print sub-DataFrame
print(cars.loc[["RU","MOR"],["country","drives_right"]])
