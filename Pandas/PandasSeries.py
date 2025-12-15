import pandas as pd 
# A Pandas Series is a 1D labeled array built on NumPy's ndarray
index = ["메로나","누가바","빠삐코"]
values = [500,800,2000]

s = pd.Series(index,values)

print(s)
print(type(s))
print(s.index)
print(s.values)