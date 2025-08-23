import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.plot(x,y)
plt.show()

plt.plot(x,y,"ro")
plt.show()

plt.plot(x,y)
plt.axis([0,10,0,200])
plt.show()

plt.plot(x,y,"r--", label="Y=X", linewidth=4)
plt.axis([0,10,0,50])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample graph")
plt.legend()
plt.show()

plt.plot([])
plt.plot([])
plt.axis([0,10,0,200])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample graph")
plt.legend()
plt.show()

import numpy as np
x=np.arange(0,10,0.2)
print(x)

y1=x**2
y2=x**3

plt.plot(x,x**2,'g--',x,x**3,'b--')
plt.show()

plt.bar([1,3,5,7],[2,4,6,9],color='b')
plt.show()

plt.bar([1,3,5,7],[2,4,6,9],color='b')
plt.bar([2,4,6,8],[3,5,7,9])
plt.show()

plt.bar(['Male Literacy','Female Literacy'],[90,95])
plt.show()