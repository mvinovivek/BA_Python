#Find the parameters of a projectile motion with duration
import math 

launch_velocity=80          #Velocity at launch, m/s
launch_angle=40             #Angle of launch, deg
g=9.81   

t=0                        #Initial time
y=0                        #Initial height
yvals=[]
xvals=[]

while y>=0:                 #If y value is less than 0, then we can say the projectile has hit the ground, so we are checking for y>0
    x=launch_velocity*t*math.cos(math.radians(launch_angle))
    y=(launch_velocity*t*math.sin(math.radians(launch_angle)))-(0.5*g*t**2)
    xvals.append(x)
    yvals.append(y)
    t+=0.01

print("Maximum Height of the Projectile is {}".format(max(yvals)))
print("Range of the Projectile is {}".format(max(xvals)))
print("Duration of Projectile is {}".format(t))

# for i in range(len(xvals)):
#     print(xvals[i],yvals[i])