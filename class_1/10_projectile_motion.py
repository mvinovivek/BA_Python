#Find the parameters of a projectile motion
import math 

launch_velocity=80          #Velocity at launch, m/s
launch_angle=40             #Angle of launch, deg
g=9.81                      #acceleration due to gravity, m2/s

max_height=((launch_velocity**2)*((math.sin(math.radians(launch_angle)))**2))/(2*g)
range=launch_velocity**2*math.sin(math.radians(2*launch_angle))/g
duration=2*launch_velocity*math.sin(math.radians(launch_angle))/g

print("The Maximum Height of the projectile is: ", max_height)
print("The Range of the projectile is: ", range)
print("The Duration of the projectile is: ", duration)