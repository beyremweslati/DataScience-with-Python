# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv("seattle_weather.csv", )
austin_weather = pd.read_csv("austin_weather.csv",)
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()