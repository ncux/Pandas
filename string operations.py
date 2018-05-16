import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')

movie_genres = movies['genres'].str.split('|', expand=True)

movie_genres[:10]

# new column inserted; the column will contain boolean values
movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')


# extract the year from the title; remember the year was in parentheses as part of the title
movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)



