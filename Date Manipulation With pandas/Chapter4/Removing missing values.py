import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle("avocado.pkl")
avocados_2016 = avocados[avocados["date"] >= "2016-01-01"]

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any().sum())