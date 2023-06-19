import matplotlib.pyplot as plt 

year = [1950,1970,1990,2010,2022,2050,2100]
population = [2.519,3.692,5.263,6.972,7.823,9.1,10]


#Add More Data
year = [1800,1850,1900] + year
population = [1.0,1.262,1.650] + population
plt.plot(year,population)


plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Word Population Projections")

plt.yticks([0,2,4,6,8,10],["0","2B","4B","6B","8B","10B "])
plt.show()
