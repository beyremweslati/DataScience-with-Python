# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,0,30)
print(prob_less_than_5)
print("-----------------------")


# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = uniform.cdf(30,0,30) - uniform.cdf(5,0,30)
print(prob_greater_than_5)
print("-----------------------")


# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20,0,30) - uniform.cdf(10,0,30)
print(prob_between_10_and_20)