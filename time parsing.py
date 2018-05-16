import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')

tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s')

greater_than_t = tags['parsed_time'] > '2015-02-01'

# sorting the order in ascending time order
tags.sort_values(by='parsed_time', ascending=True)[:10]

