# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
gdp_cap = [500,1000,2000,5000,10000,20000,50000]
life_exp = [45,53,60,65,73,77,83]
# Make a line plot: year on the x-axis, pop on the y-axis
plt.scatter(gdp_cap,life_exp)
# Display the plot with plt.show()
plt.xscale("log")
plt.show()