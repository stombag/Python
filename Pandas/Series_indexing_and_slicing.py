import pandas as pd 

data = [100,200,300]    
index = ["월","화","수"]
s = pd.Series(data, index)
print(s.iloc[0])
print(s.iloc[1])
print(s.iloc[2])
print(s.iloc[-1])
s.loc["월"]
s.loc["화"]
s.loc["수"]

print(s)
print(s["월"])
print(s.iloc[0:2])
print(s.loc["화":"수"])

print(s.iloc[[0,2]])
#loc / iloc can select non-contiguous data by passing a list of labels/positions.