import pandas as pd
import numpy as np
amir_deals = pd.read_csv("amir_deals.csv")

# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)


# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace= True)
print(sample_with_replacement)