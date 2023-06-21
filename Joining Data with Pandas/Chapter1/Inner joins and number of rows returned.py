import pandas as pd

wards = pd.read_pickle('ward.p')
census = pd.read_pickle('census.p')


# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on="ward")

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)