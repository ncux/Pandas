import pandas as pd

data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora': 10, 'alice': 20}]

data_DF = pd.DataFrame(data)

print(data_DF)

print(data_DF.index)

data_DF2 = pd.DataFrame(data,  index=['accord', 'camry'])

print(data_DF2)

data_DF3 = pd.DataFrame(data,  columns=['joe', 'dora','alice'])

print(data_DF3)



