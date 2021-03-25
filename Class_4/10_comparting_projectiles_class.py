import numpy as np
import matplotlib.pyplot as plt


class projectile():
    g=9.81
    def __init__(self,launch_angle,launch_velocity):
        self.launch_angle=launch_angle
        self.launch_velocity=launch_velocity

    def duration(self):
        duration=2*self.launch_velocity*np.sin(np.radians(self.launch_angle))/self.g
        return duration

    def range_dist(self):
        range_dist=self.launch_velocity**2*np.sin(np.radians(2*self.launch_angle))/self.g
        return range_dist

    def ceiling(self):
        ceiling=((self.launch_velocity**2)*((np.sin(np.radians(self.launch_angle)))**2))/(2*self.g)
        return ceiling

    def coordinates(self):
        duration_val = self.duration()
        t=np.linspace(0,duration_val,100)
        x=self.launch_velocity*t*np.cos(np.radians(self.launch_angle))
        y=(self.launch_velocity*t*np.sin(np.radians(self.launch_angle)))-(0.5*self.g*t**2)

        return x,y

angle=20
velocity=50
our_projectile=projectile(angle,velocity)
print("Range of projectile with V={} m/s,launched at {} degrees is {} m".format(velocity,angle, our_projectile.range_dist()))
print("Ceiling of projectile with V={} m/s,launched at {} degrees is {} m".format(velocity,angle, our_projectile.ceiling()))
print("Duration of projectile with V={} m/s,launched at {} degrees is {} s".format(velocity,angle, our_projectile.duration()))
X,Y=our_projectile.coordinates()
plt.plot(X,Y)
plt.xlabel("Range, m")
plt.ylabel("Altitude, m")
plt.title("A projectile")
plt.show()


# launch_angles=[10,20,30]
# launch_velocities=[50,100,150]

# for angle in launch_angles:
#     for velocity in launch_velocities:
#         our_projectile=projectile(angle,velocity)
#         # print("Range of projectile with V={} m/s,launched at {} degrees is {} m".format(velocity,angle, our_projectile.range_dist()))
#         # print("Ceiling of projectile with V={} m/s,launched at {} degrees is {} m".format(velocity,angle, our_projectile.ceiling()))
#         # print("Duration of projectile with V={} m/s,launched at {} degrees is {} s".format(velocity,angle, our_projectile.duration()))
#         # print('\n\n')
#         x,y=our_projectile.coordinates()
#         plt.plot(x,y,label="V= {}, T={}".format(angle,velocity))

# plt.title("Comparing Projectiles")
# plt.xlabel("Range, m")
# plt.ylabel("Altitude, m")
# plt.legend()
# plt.show()