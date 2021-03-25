#We are extending the projectile problem with plots for better visibility
import numpy as np
import matplotlib.pyplot as plt

launch_angle=40
launch_velocity=100
g=9.81

duration=2*launch_velocity*np.sin(np.radians(launch_angle))/g
t=np.linspace(0,duration,100)

x=launch_velocity*t*np.cos(np.radians(launch_angle))
y=(launch_velocity*t*np.sin(np.radians(launch_angle)))-(0.5*g*t**2)

plt.plot(x,y)
plt.title("A Projectile")
plt.xlabel("Range, m")
plt.ylabel("Altitude, m")
plt.show()

#Comparing two projectiles
launch_angle_1=40
launch_angle_2=60
launch_velocity=100
g=9.81

duration_1=2*launch_velocity*np.sin(np.radians(launch_angle_1))/g
duration_2=2*launch_velocity*np.sin(np.radians(launch_angle_2))/g
t1=np.linspace(0,duration_1,100) 
t2=np.linspace(0,duration_2,100) 

x_1=launch_velocity*t1*np.cos(np.radians(launch_angle_1))
y_1=(launch_velocity*t1*np.sin(np.radians(launch_angle_1)))-(0.5*g*t1**2)

x_2=launch_velocity*t2*np.cos(np.radians(launch_angle_2))
y_2=(launch_velocity*t2*np.sin(np.radians(launch_angle_2)))-(0.5*g*t2**2)

plt.plot(x_1,y_1, label="V = {}, Theta ={}".format(launch_velocity,launch_angle_1))
plt.plot(x_2,y_2, label="V = {}, Theta ={}".format(launch_velocity,launch_angle_2))
plt.title("Comparing Projectiles")
plt.xlabel("Range, m")
plt.ylabel("Altitude, m")
plt.legend()
plt.show()