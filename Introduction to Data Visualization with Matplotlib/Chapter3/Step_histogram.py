# Import pandas as pd
import pandas as pd 
import matplotlib.pyplot as plt


mens_rowing = pd.read_csv("mens_rowing.csv", index_col=0)
mens_gymnastics = pd.read_csv("mens_gymnastics.csv", index_col=0)

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], label="Rowing", histtype='step', bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], label="Gymnastics", histtype='step', bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()