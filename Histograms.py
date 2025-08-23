import matplotlib.pyplot as plt

ages=[56,88,34,12,33,49,67,71]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins,histtype='bar', rwidth=0.5)
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

x=[1,2,3,4,5,6,7,8,9]
y=[0,1,0,1,0,1,0,1,0]

plt.scatter(x,y,label="Scatter Plot",color="red",marker="*",s=50)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Plot")
plt.legend()
plt.show()