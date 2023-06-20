import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle("avocado.pkl")

# Histogram of conventional avg_price
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5,bins=20)

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5,bins=20)

# Add a legend
plt.legend(["conventional", "organic"])


# Show the plot
plt.show()


