import pandas as pd

ratings = pd.read_csv('/home/malaba/Documents/MovieLens ml-20m/ratings.csv')

histogram = ratings.hist(column='rating', figsize=(15,10))

boxplot = ratings.boxplot(column='rating', figsize=(15,20))

print(histogram)



