import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle("avocado.pkl")
avocados_2016 = avocados[avocados["date"] >= "2016-01-01"]


cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()


# Show the plot
plt.show()