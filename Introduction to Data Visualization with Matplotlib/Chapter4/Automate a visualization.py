import pandas as pd 
import matplotlib.pyplot as plt


summer_2016_medals = pd.read_csv("summer2016.csv",index_col=0)
# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
    # Extract the rows only for this sport
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    # Add a bar for the "Weight" mean with std y error bar
    ax.bar(sport,sport_df["Weight"].mean(),yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)
fig.set_size_inches(12,10)
# Save the figure to file
fig.savefig("sports_weights.png")