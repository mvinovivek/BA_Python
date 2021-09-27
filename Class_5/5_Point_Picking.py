import matplotlib.pyplot as plt
import mplcursors
import numpy as np

Xvals=np.linspace(0,2*np.pi,50)
Yvals=np.sin(Xvals)
ZVals=np.cos(Xvals)


#Creating the Plot
fig = plt.figure()
ax = fig.add_subplot(111)


ax.plot(Xvals,Yvals,label="Sin Curve")
ax.plot(Xvals,ZVals,label="Cos Curve")
ax.plot(Xvals,ZVals*2,label="T Curve")
ax.plot(Xvals,ZVals/2,label="T1 Curve")
ax.plot(Xvals,ZVals*3,label="T2 Curve")

c2=mplcursors.cursor(multiple=True)

@c2.connect("add")
def _(sel):
    sel.annotation.get_bbox_patch().set(fc="yellow")
    coordinates=sel.target
    label=sel.artist.get_label()
    #This will change how the annotation will look like
    sel.annotation.set_text(label+'\n'+str(round(coordinates[0],2))+'\n'+str(round(coordinates[1],2)))
    # sel.annotation.set_text("This is selected")
    


plt.legend()
plt.show()