import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')

ratings_count = ratings[['movieId','rating']].groupby('rating').count()

average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()

movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()

movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()