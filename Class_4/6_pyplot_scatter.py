#pyplot comes with many inbuilt plots. we will use the scatter method to produce scatter plots

#importing the plotting library from the matplotlib and renaming that as plt for convenience
import matplotlib.pyplot as plt 
import numpy as np


# By default scatter plots always needs two values

# Creating values to plot
X=np.linspace(0,2*np.pi,100)
Y=np.sin(X)

# Simple scatter plot
plt.scatter(X,Y)
plt.show()

# now we can see that scatter plot marker is not that great and it is too small. Lets make it bigger and change the style also

# Scatter plot options
plt.scatter(X,Y, marker='o',  s=4)
plt.show()

# much better now??

# Like the simple plot, scatter plot also gives us more options to style them
# #More scatter plot options
#plots with legends
X=np.random.randint(200, size=(20))
Y=np.random.randint(200, size=(20))
Z=np.random.randint(200, size=(20))

# Color argument as usual will set the color of the scatter marker

# Marker argument will set the style of the scatter
# There are so many options available. we can find them here https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers

plt.scatter(X,Y, color='green',marker='>', label="Data 1", s=50)
plt.scatter(X,Z, color='red', marker='p',label="Data 2", s=30)
plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("Some random scatters")
plt.legend()
plt.legend(title="Title")
plt.show()

# Now we can reduce the opacity of the plots using alpha which will take the values from 0 to 1. 1 is opaque and 0 is fully transparent
# One of the coolest thing about scatter plot is that, we can create stunning bubble charts with minimum change in the code

#lets create some data
X=np.linspace(0,10,30)
Y=X**2
Z=X**3

plt.scatter(X,Y,color='blue', label="Squared")   
plt.scatter(X,Z,color='orange', label ="Cubed")

plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("Some random scatters")
plt.legend()
plt.show()

#Now we can increase the size of the scatter to account for the change in the value
X=np.linspace(1,10,20)
Y=X**2
Z=X**3

#Normalizing data
Y_normal=Y/max(Y)
Z_normal=Z/max(Z)

plt.scatter(X,Y,color='darkblue', label="Squared", s=Y_normal*500, alpha=0.5)   
plt.scatter(X,Z,color='purple', label ="Cubed", s=Z_normal*500, alpha=0.5)

plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("Nice Bubble Plot!")
plt.show()


#We can combine line plot and scatter plot to enhance the visualization
X=np.random.randint(1,100,20)
Y=np.random.randint(1,100,20)

# plt.plot(X,Y,linestyle='dotted', color='b')
# plt.scatter(X,Y, color='red')
# plt.show()

dictionary={}
#Handy dictionary
for i in range(len(X)):
    dictionary[X[i]]=Y[i]

X_Sorted=[]
Y_Sorted=[]
for i in sorted(dictionary.keys()):
    X_Sorted.append(i)
    Y_Sorted.append(dictionary[i])

plt.plot(X_Sorted,Y_Sorted,linestyle='dotted', color='b')
plt.scatter(X_Sorted,Y_Sorted, color='red')
plt.show()