import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')

is_highly_rated = ratings['rating'] >= 4.0

ratings[is_highly_rated][30:50]

is_animation = movies['genres'].str.contains('Animation')

movies[is_animation][5:15]