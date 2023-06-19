# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# subset cars: sel
sel = cars[cars["drives_right"]]
# Print sel
print(sel)
