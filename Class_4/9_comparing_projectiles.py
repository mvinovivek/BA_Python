import numpy as np
import matplotlib.pyplot as plt

launch_angles=np.array([30,40,50,60])
launch_velocity=100
g=9.81
X=[]
Y=[]
t_values=[]

durations=2*launch_velocity*np.sin(np.radians(launch_angles))/g

for duration in durations:
    t_values.append(np.linspace(0,duration,100))

for i in range(len(t_values)):
    t=t_values[i]
    launch_angle=launch_angles[i]
    x=launch_velocity*t*np.cos(np.radians(launch_angle))
    y=(launch_velocity*t*np.sin(np.radians(launch_angle)))-(0.5*g*t**2)

    X.append(x)
    Y.append(y)


for i in range(len(X)):
    plt.plot(X[i],Y[i], label="V = {}, Theta ={}".format(launch_velocity, launch_angles[i]))

plt.title("Comparing Projectiles")
plt.xlabel("Range, m")
plt.ylabel("Altitude, m")
plt.legend()
plt.show()