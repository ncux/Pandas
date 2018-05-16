import pandas as pd

# create a data frame from a dictionary of python series

d = {'one' : pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two' : pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}

dataFrame = pd.DataFrame(d)

print(dataFrame)

print(dataFrame.index)   # ['apple', 'ball', 'cerill', 'clock', 'dancy']
print(dataFrame.columns)   # ['one', 'two']