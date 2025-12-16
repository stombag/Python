from pandas import Series
s = Series([100,200,300,400,500])

#Broadcasting
print(s+10)
high = Series (data=[51500,51200,52500], index=["5/1","5/2","5/3"])
low = Series (data =[50700,50500,50050,], index=["5/1","5/2","5/4"])

diff = high - low
print(diff)

# comparison operation

cond = s >300
print(cond)

# filtering 
print(s[cond])


#Q1
smell = Series([10,200,200,400,600])
big = Series([100,300,400,500,600])

result1 = (big - smell) >=100
print(big[result1],"Q1")

#Q2
lastValue= Series([93000,82400,99100,81000,72300],['05/14','05/15','05/16','05/17','05/18'])
result = (lastValue<90000)& (lastValue>=80000)
print(lastValue[result].index,"Q3")

