# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv("seattle_weather.csv", )
austin_weather = pd.read_csv("austin_weather.csv",)
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()
# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b", marker='o', linestyle="--")

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r", marker="v", linestyle="--")

# Call show to display the resulting plot
plt.show()