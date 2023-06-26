import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
world_happiness = pd.read_csv("world_happiness.csv")

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x="gdp_per_cap",y="happiness_score",data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness["happiness_score"].corr(world_happiness["gdp_per_cap"])
print(cor)

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness["gdp_per_cap"])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x="log_gdp_per_cap",y="happiness_score",data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness["log_gdp_per_cap"].corr(world_happiness["happiness_score"])
print(cor)