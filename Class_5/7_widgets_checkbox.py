import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

Xvals=np.linspace(0,2*np.pi,50)
Yvals=np.sin(Xvals)
Zvals=np.cos(Xvals)

#Creating the Plot
# Plotting
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(right=0.8)
sin,=ax.plot(Xvals,Yvals)
cos,=ax.plot(Xvals,Zvals)
plt.title("Check Buttons")


plots =[sin,cos]
activated = [True, True]
labels = ['Sin Curve', 'Cos Curve']

# instance the axes
ax_check = plt.axes([0.81, 0.5, 0.18, 0.25])
plot_button = CheckButtons(ax_check,labels, activated)


# function for displaying/hiding the plots
def select_plot(label):
    
    # get the index that corresponds to the word "label"
    index = labels.index(label)
    
    # set the plot to visible
    plots[index].set_visible(not plots[index].get_visible())
    fig.canvas.draw()

    
plot_button.on_clicked(select_plot)
plt.show()