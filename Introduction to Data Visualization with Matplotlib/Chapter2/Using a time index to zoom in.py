import pandas as pd 
import matplotlib.pyplot as plt

climate_change = pd.read_csv("climate_change.csv", parse_dates=True, index_col="date")
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])


# Show the figure
plt.show()