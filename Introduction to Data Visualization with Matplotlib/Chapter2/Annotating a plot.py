import pandas as pd 
import matplotlib.pyplot as plt

climate_change = pd.read_csv("climate_change.csv", parse_dates=True, index_col="date")
fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change["relative_temp"])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", xy=[pd.Timestamp('2015-10-06'), 1] )

plt.show()