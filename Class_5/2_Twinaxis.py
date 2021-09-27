import numpy as np 
import matplotlib.pyplot as plt 

X=np.random.randint(10,100,20)
X=np.sort(X)
Y=X+X**2
Z=2*X**4

# ax=plt.subplot(111)
# ax.plot(X,Y)
# ax.plot(X,Z)
# plt.show()

# ax=plt.subplot(111)
# ax.plot(X,Y,label="First Graph",color="green")


# # ax2=plt.twinx(ax)
# ax2=ax.twinx()


# ax2.plot(X,Z, label="Second Graph",color="purple")
# ax.legend(loc=1)
# ax2.legend(loc=2)
# ax2.set_ylabel("This is custom")
# plt.show()



fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(X,Y,label="First Graph",color="green")
#ax2=plt.twinx(ax)
ax2=ax.twinx()
ax2.plot(X,Z, label="Second Graph",color="purple")

fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)

plt.show()
# %%
