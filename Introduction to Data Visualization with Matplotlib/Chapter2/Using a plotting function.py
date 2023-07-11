import pandas as pd 
import matplotlib.pyplot as plt

climate_change = pd.read_csv("climate_change.csv", parse_dates=True, index_col="date")


# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

    # Plot the inputs x,y in the provided color
    axes.plot(x, y, color=color)

    # Set the x-axis label
    axes.set_xlabel(xlabel)
    
    # Set the y-axis label
    axes.set_ylabel(ylabel, color=color)
    
    # Set the colors tick params for y-axis
    axes.tick_params('y', colors=color)


fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change["relative_temp"], "red", "Time (years)", "Relative temperature (Celsius)")

plt.show()