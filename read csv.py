import pandas as pd

movies = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/movies.csv')
ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')
tags = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/tags.csv')


#print(movies.head(10))
#print(ratings.head(10))
#print(tags.head(10))

del ratings['timestamp']
del tags['timestamp']

#Extract 0th row: notice that it is infact a Series

tagsrow_0 = tags.iloc[0]
print(tagsrow_0)
print(tagsrow_0.index)

