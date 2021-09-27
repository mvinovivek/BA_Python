import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

Xvals=np.linspace(0,2*np.pi,50)
Yvals=np.sin(Xvals)
ZVals=np.cos(Xvals)

#Creating the Plot
# Plotting
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(bottom=0.2)

ax.plot(Xvals,Yvals,label="Sin Curve")
ax.plot(Xvals,ZVals,label="Cos Curve")

button=Button(plt.axes([0.12, 0.1, 0.08, 0.05]),'Grid',color='orange', hovercolor='green')
button1=Button(plt.axes([0.22, 0.1, 0.08, 0.05]),'Minor Grid',color='orange', hovercolor='green')


# enabling/disabling the grid
def grid(val):
    ax.grid()
    fig.canvas.draw() #redraw the figure

minor =True
def minor(val):
    global minor
    if minor:
        ax.minorticks_off()
        minor=False
    else:
        ax.minorticks_on()

    ax.grid(which='minor')
    fig.canvas.draw() #redraw the figure

# triggering event is the clicking
button.on_clicked(grid)
button1.on_clicked(minor)
plt.show()