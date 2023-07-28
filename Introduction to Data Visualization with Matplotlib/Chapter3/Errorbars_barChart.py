# Import pandas as pd
import pandas as pd 
import matplotlib.pyplot as plt

mens_rowing = pd.read_csv("mens_rowing.csv", index_col=0)
mens_gymnastics = pd.read_csv("mens_gymnastics.csv", index_col=0)

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())


# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()