import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

# Set random seed to 334
np.random.seed(334)

# Import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()