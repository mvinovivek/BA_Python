import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

Xvals=np.linspace(0,2*np.pi,50)
Yvals=np.sin(Xvals)
Zvals=np.cos(Yvals)

#Creating the Plot
# Plotting
fig = plt.figure()
ax = fig.subplots()
plt.subplots_adjust(right=0.8)

line,=ax.plot(Xvals,Yvals)
plt.title("Click the Radio Button to Change the Colors")

ax_color = plt.axes([0.81, 0.5, 0.18, 0.25])
color_button = RadioButtons(ax_color, ['red', 'green', 'blue', 'black', 'orange'],[False, False, True, False], activecolor= 'k')

# function for changing the plot color
def color(labels):
    line.set_color(labels)
    fig.canvas.draw()

color_button.on_clicked(color)
plt.show()