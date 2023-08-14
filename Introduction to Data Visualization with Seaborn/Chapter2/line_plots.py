# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

mpg = pd.read_csv("mpg.csv")
# Create line plot
sns.relplot(x="model_year",y="mpg",data=mpg,kind="line")
# Show plot
plt.show()