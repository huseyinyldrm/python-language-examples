import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[10,15,20,25,30]
y2=[5,10,15,20,25]

plt.fill_between(x,y1,y2,color="green",alpha=0.4)
plt.title("Area Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()