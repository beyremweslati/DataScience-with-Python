import pandas as pd
import matplotlib.pyplot as plt


# Create the years and durations lists
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]

# Create a dictionary with the two lists
movie_dict = {
    "years" : years,
    "durations" : durations
}

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)


#fig = plt.figure()
# Draw a line plot of release_years and durations
#plt.plot(durations_df['years'],durations_df["durations"])
# Create a title
#plt.title("Netflix Movie Durations 2011-2020")
# Show the plot
# plt.show()

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[["title","country","genre","release_year","duration"]]


# Create a figure and increase the figure size
#fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
#plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"])
# Create a title
#plt.title("Movie Duration by Year of Release")

# Show the plot
#plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]


# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"],netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")


# Show the plot
plt.show()