# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv("seattle_weather.csv", )
austin_weather = pd.read_csv("austin_weather.csv",)
# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])


# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()