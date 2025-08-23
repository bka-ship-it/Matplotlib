slices=[6,12,1,3]
activities=["sleeping","eating","working","watching tv","working out"]
cols=["c","m","r","b","g"]

import matplotlib.pyplot as plt
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True)
plt.title("Day Chart")
plt.show()

days=[1,2,3,4,5]
eating=[2,3,4,3,2]
sleeping=[7,8,6,11,7]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([],[],color="m",label="Eating",linewidth=5)
plt.plot([],[],color="c",label="Sleeping",linewidth=5)
plt.plot([],[],color="r",label="Working",linewidth=5)
plt.plot([],[],color="k",label="Playing",linewidth=5)
plt.stackplot(days,eating,sleeping,working,playing,colors=['m','c','r','k'])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Stack Plot")
plt.legend()
plt.show()