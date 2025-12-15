import pandas as pd

data = [100,200,300]
index = ["월","화","수"]
s = pd.Series(data,index )

#Add
s['목'] = 400
print(s)
s.loc['금'] = 500
print(s)

#Delet
print(s.drop('목'))
print(s)
s.drop('목', inplace=True)
print(s)
print(s.drop(['수', '금']))


#modify
s['수']=3000

print(s)

s.iloc[3] = 4000

print(s)
s.loc['월'] = 5000

print(s)