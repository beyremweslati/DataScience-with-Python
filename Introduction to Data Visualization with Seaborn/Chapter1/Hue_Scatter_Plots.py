# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv("student-alcohol-consumption.csv")
# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3",data=student_data,hue="location")



# Show plot
plt.show()