# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("countries-of-the-world.csv")
# Create count plot with region on the y-axis
sns.countplot(y="Region",data=df)

# Show plot
plt.show()