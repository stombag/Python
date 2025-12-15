import numpy as np

price = [
    [100,80,40,30],
    [120,110,100,102]
]
#print(print[0])
#Printing a 2D list in Python is possible, bot not easy to read
#Numpy prihnts 2D arrays in a clear matrix form

arr2 = np.array(price)
print(arr2[0])
print(arr2[1])

#indexing == aparticular value 
print(arr2[1][0])
print(arr2[0][3])

# ':' means all rows, '0' means the thrst column
print(arr2[:,0])
print(arr2[1,:])