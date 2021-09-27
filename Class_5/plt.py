import matplotlib.pyplot as plt 
import numpy as np

X=np.linspace(0,2*np.pi,100)
cosVals=np.cos(X)
sinVals=np.sin(X)


plt.plot(X,cosVals)

plt.minorticks_on()
plt.grid(which='both')
plt.xlabel("X axis", fontsize=24) 
plt.ylabel("Y axis") 
plt.show()