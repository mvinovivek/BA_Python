#Solving Tsiolkovsky Rocket Equation

#importing math library for more functions
import math 

isp=300                 #Specific Impulse in s
initial_mass=100         #Initial mass of spacecraft, kg
mdot=0.5                #Mass of propellant consumed, kg/s
burn_time=30            #Duration of engine burning
g_0=9.81                #gravitational acceleration constant 


final_mass=initial_mass-(mdot*burn_time)
V_eff=isp*g_0

delta_V= V_eff*math.log(initial_mass/final_mass)

print("Velocity Imparted to the Spacecraft is: {} m/s".format(delta_V))