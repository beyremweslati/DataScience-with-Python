# Import binom from scipy.stats
from scipy.stats import binom
import numpy as np
# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1,0.3,size=1))
print("--------------------")


# Simulate 1 week of 3 deals
print(binom.rvs(3,0.3,size=1))
print("--------------------")

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.3,size=52)
# Print mean deals won per week
print(deals.mean())
