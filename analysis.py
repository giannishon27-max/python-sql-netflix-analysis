import pandas as pd

# load dataset
df = pd.read_csv("data/netflix_titles.csv")

# basic info
print("Dataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst rows:")
print(df.head())

# count movies vs tv shows
print("\nMovies vs TV Shows:")
print(df["type"].value_counts())

# top countries
print("\nTop countries:")
print(df["country"].value_counts().head(10))

# most common ratings
print("\nRatings:")
print(df["rating"].value_counts().head(10))
