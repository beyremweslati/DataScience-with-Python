import pandas as pd
sales = pd.read_csv("sales.csv")


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store","type"])
# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store","department"])

# Count the number of stores of each type

store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort= True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)