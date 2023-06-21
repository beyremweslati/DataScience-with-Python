import pandas as pd

wards = pd.read_pickle('ward.p')
licenses = pd.read_pickle('licenses.p')
zip_demo = pd.read_pickle('zip_demo.p')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on="zip") \
            			.merge(wards, on="ward")

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby("alderman").agg({'income':'median'}))