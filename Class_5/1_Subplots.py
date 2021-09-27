import matplotlib.pyplot as plt 
import numpy as np

X=np.linspace(0,2*np.pi,100)
cosVals=np.cos(X)
sinVals=np.sin(X)

# plt1=plt.subplot(2,1,1) # Row, Column, Graph Number
# plt2=plt.subplot(2,1,2)
# plt1.plot(X,sinVals)
# plt2.plot(X,cosVals)
# plt1.set_title("Sine Curve")
# plt2.set_title("Cos Curve")
# plt.tight_layout()
# plt.show()


# %%
#This is same as above, but we are creating a figure and then adding the subplots. This will
# #help us to adjust the size of the final output based on our needs
# figure=plt.figure(figsize=(4,5))
# plt1=figure.add_subplot(2,1,1)
# plt2=figure.add_subplot(2,1,2)
# plt1.plot(X,sinVals)
# plt2.plot(X,cosVals)
# plt1.set_title("Sine Curve")
# plt2.set_title("Cos Curve")
# figure.tight_layout()
# plt.show()


# #Row wise plotting
# plt1=plt.subplot(1,2,1)
# plt2=plt.subplot(1,2,2)
# plt1.plot(X,sinVals)
# plt2.plot(X,cosVals)
# plt1.set_title("Sine Curve")
# plt2.set_title("Cos Curve")
# plt.tight_layout()
# plt.show()

# # # # %%
# figure=plt.figure(figsize=(12,4))
# plt1=figure.add_subplot(1,2,1)
# plt2=figure.add_subplot(1,2,2)
# plt1.plot(X,sinVals)
# plt2.plot(X,cosVals)
# plt1.set_title("Sine Curve")
# plt2.set_title("Cos Curve")
# figure.tight_layout()
# plt.show()


# # %%
#Creating an array of plots 
import numpy as np 
import matplotlib.pyplot as plt
X=np.random.randint(10,100,20)

fig=plt.figure(figsize=(8,6))
for i in range(1,10):
    subplt=fig.add_subplot(3,3,i)
    if i%2==0:
        subplt.scatter(X,(i+1)*X)
    else:
        subplt.plot(X,(i+1)*X)
    subplt.set_title("Plot {}".format(i))
    subplt.set_xlabel("X Axis of {}".format(i))
    subplt.set_ylabel("Y Axis of {}".format(i))


plt.suptitle("A plot grid!")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()