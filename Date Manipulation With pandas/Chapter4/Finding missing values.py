import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle("avocado.pkl")
avocados_2016 = avocados[avocados["date"] >= "2016-01-01"]
# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()