import matplotlib.pyplot as plt

plt.figure
plt.plot([10,20,30,40,60,40,70,200,300])
plt.show()


data = [10,20,30,50,70,90,100,200,300]
plt.figure(figsize=(10,5))
plt.plot(data,color='green', linestyle='dashed',marker='o',markerfacecolor='red',markersize='15')
plt.show()

