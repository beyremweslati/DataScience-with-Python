import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# Set seed to 321
np.random.seed(321)

amir_deals = pd.read_csv("amir_deals.csv")
all_deals = pd.read_csv("all_deals.csv")
sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals["num_users"].sample(20,replace=True)
  # Take mean of cur_sample
  cur_mean = cur_sample.mean()
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(amir_deals["num_users"].mean())