# Import pandas as pd
import pandas as pd 
import matplotlib.pyplot as plt


medals = pd.read_csv("medals.csv", index_col=0)
fig, ax = plt.subplots()
# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"], bottom=medals["Gold"] + medals["Silver"], label="Bronze")
# Display the legend
ax.legend()
plt.show()