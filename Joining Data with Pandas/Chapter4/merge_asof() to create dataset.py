import pandas as pd
import matplotlib.pyplot as plt
gdp = pd.read_csv("GDP.csv",index_col=0)
recession = pd.read_csv("recession.csv", index_col=0)
gdp["date"] = pd.to_datetime(gdp["date"])
recession["date"] = pd.to_datetime(recession["date"])
# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp,recession,on="date")

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()