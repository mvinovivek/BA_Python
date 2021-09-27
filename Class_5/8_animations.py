import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata =[1,2,3,4,5,6]
ydata = [5,6,7,5,9,6]
ln, = plt.plot([], [], 'r')

def function():
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1, 1)
    return ln,


def update(frame):
    data=[]
    with open("data.txt",'r') as testfile:
        lines=testfile.readlines()
        for line in lines:
           data.append(line.split(","))
           
    xdata=data[0]
    xvals=[]
    for x in xdata:
        xvals.append(float(x))
    ydata=data[1]
    yvals=[]
    for y in ydata:
        y.replace("\n","")
        yvals.append(float(y))

    ln.set_data(xvals, yvals)
    ax.set_xlim(0, max(xvals))
    ax.set_ylim(min(yvals), max(yvals))

    return ln,

ani = FuncAnimation(fig, update, frames=100, init_func=function, blit=True)
plt.show()