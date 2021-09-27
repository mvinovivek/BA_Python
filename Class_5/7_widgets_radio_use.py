import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

Xvals=np.linspace(0,2*np.pi,50)
Yvals=np.sin(Xvals)
Zvals=np.cos(Xvals)

#Creating the Plot
# Plotting
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(right=0.8)


plt.title("Click the Radio Button to Change the Colors")

ax_color = plt.axes([0.81, 0.5, 0.18, 0.25])
color_button = RadioButtons(ax_color, ['sin', 'cos'],[True, False], activecolor= 'k')

# function for changing the plot color
def color(curve):
    if curve=="sin": 
        ax.clear()       
        ax.plot(Xvals,Yvals)
        ax.set_title("Sine Curve")
        fig.canvas.draw()

    elif curve =="cos":
        ax.clear()
        ax.plot(Xvals,Zvals)
        ax.set_title("Cos Curve")
        fig.canvas.draw()

    else:
        pass

color_button.on_clicked(color)
plt.show()