import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')

#is any row NULL ?
movies.shape
movies.isnull().any()

ratings.shape
ratings.isnull().any()

tags.shape
tags.isnull().any()

# remove invalid or missing data
tags = tags.dropna()