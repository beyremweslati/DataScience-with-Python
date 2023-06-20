import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle("avocado.pkl")

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
print(nb_sold_by_date)
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot()

# Show the plot
plt.show()