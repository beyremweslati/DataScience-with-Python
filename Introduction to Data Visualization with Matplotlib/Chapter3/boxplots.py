# Import pandas as pd
import pandas as pd 
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv("mens_rowing.csv", index_col=0)
mens_gymnastics = pd.read_csv("mens_gymnastics.csv", index_col=0)

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"],mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing","Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()