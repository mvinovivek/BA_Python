#There are many plotting libraries available in python. We will use the so called grandfather of all the plotting libraries. The "matplotlib" library. 
#matplotlib is a vast library with so many front end and backend tools. The most commonly used tool to plot is the pyplot. We will use the same here

#importing the plotting library from the matplotlib and renaming that as plt for convenience
import matplotlib.pyplot as plt 
import numpy as np


# Plotting a single array
#Pyplot with simple plot will create line plots of the values. Line plots are the universal basic plots
#pyplot works with single value as in it can plot a series od data or plot two data against each other (Simple XY Plot)
#Now lets start with plotting a single series of data

#for this i am creating a dummy array of 10 integer values using the numpy random method
x=np.random.randint(100, size=(10))

#You can see the data by this
print(x)


#Now we just plot it. 
plt.plot(x)
plt.show()

# It is as simple as that. Now based on where you had run this you will see the difference in the plot output. VS Code, Pycharm, Idle will generate a new windor for the plot
#and spyder and jupyter will create the plot inline meaning no separate window for the plots



# Plotting Two values against each other. The Simple XY plot
#Now we will create two series of data, one value of angles and other is their sin value
X=np.linspace(0,2*np.pi,100)
Y=np.sin(X)

#Now you need to pass two variables to plot them against each other
plt.plot(X,Y)
plt.show()


#Our plot looks pretty dull isn't it? 
#lets add some more elements to the plot

# Plot Option example
X=np.linspace(0,2*np.pi,100)
Y=np.sin(X)

plt.plot(X,Y)

#To set the name of the X Axis we need to use, xlabel method
plt.xlabel("This is X label")

#To set the name of the Y Axis we need to use, ylabel method
plt.ylabel("This is Y Label")

#To set the Title for our plot, we need to use, title method
plt.title("This is a Sine Curve")

#Then we can show the plot
plt.show()

#The graph looks more useful now!!
#But the line color is not spirited
#We can modify the line 

#Line options Example
X=np.linspace(0,2*np.pi,100)
Y=np.sin(X)


#To change the style of the line, we need to use the linestyle option
#Available linestyles are ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']

#To change the color of the line we need use color argument
#matplot offers tons of colors to use. You can see them all here https://matplotlib.org/stable/gallery/color/named_colors.html
#You can also use any rgb color you want (we will cover later)

#To change the width of the line we can use the linewidth parameter, it can work with int and floats also
plt.plot(X,Y, linestyle='dashed', color='green', linewidth='3.2')
plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("This is a Sine Curve")
plt.show()



#Now that we have mastered the basics of the line plot we will move to next topic
#how to we compare two sets of data. Two series in the same plot?
#we can easily do that. Before calling the plot.show() whatever we plot will be added in the same figure
#Multi line Example

#Creating some X data
X=np.linspace(0,4*np.pi,100)

#Creating some Y Data
Y=np.sin(X)

#Creating some Z data
Z=np.cos(X)


#PLotting the first series of data against each other
plt.plot(X,Y, color='green')

#plotting the second series of data before calling the show!!!
#This will add the plot in the same figure
plt.plot(X,Z, color='red')

#Usual customization
plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("Sine and Cos Curves")
plt.show()

#Yup it is simple as that. You can plot any number of data series in the same figure using this method
#But we do have some confusions here! What line is what? we need to name them?

#we can do them by using the label parameter while plotting. This way the plot will have the name 
#plots with legends
X=np.linspace(0,4*np.pi,100)
Y=np.sin(X)
Z=np.cos(X)

#For the first curve, which is the sin value of X,I name Sin curve
plt.plot(X,Y, color='green', label="Sine Curve")

#For the second curve, which is the cos value of X,I name Sin curve
plt.plot(X,Z, color='red', label="Cos Curve")


#Usual addins
plt.xlabel("This is X label")
plt.ylabel("This is Y Label")
plt.title("Sine and Cos Curves")

#Now this following command will put the labels inside the figure. If we are not calling this, then we will not see the labels
plt.legend()

#Variation in the legend function

#To add legend title
plt.legend(title="Title")

#To position the legend
plt.legend(loc=4)

#All the legend locations can be found at https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.show()


#Best practice while creating graph
#Don't change the color of the line, but change the line style
#If you are changing colors, make sure they are consistent in all plots in the study
#Don't use black color for any data series in the color plots, use black only for constant values, example nozzle contour
#There are font customization available, we need to make use of them to make the data look visible in any document