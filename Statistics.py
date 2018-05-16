import pandas as pd

ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')

#print(ratings)
#print(ratings['rating'])
print(ratings.describe())
print('\n')
print(ratings['rating'].describe())
print('\n')
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())
print(ratings['rating'].std())
print(ratings['rating'].mode())
print('\n')
filter1 = ratings['rating'] > 4
print(filter1)









