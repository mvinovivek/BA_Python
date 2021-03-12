#This program finds the variation of atmospheric pressure with altitude
#The program uses the barometric formula
#formula and data is taken from https://en.wikipedia.org/wiki/Barometric_formula

import math

Height_Slaps=(0.0,11000,20000,32000,47000,51000,71000)
Pb_Slaps=(101325.0,22632.0,5474.89,868.02,110.91,66.94,3.96)
Tb_Slaps=(288.15,216.65,216.65,288.65,270.65,270.65,214.65)
L_Slaps=(-0.0065,0.0,0.001,0.0028,0.0,-0.0028,-0.002)


g0=9.81
M=0.0289644             #kg/mol
R=8.3144598             #J/mol K


hvals=[]                #empty array to hold the altitude values
pvals=[]                #empty array to hold the pressure values
max_altitude=60e3       #Maximum altitude in m
increment=100           #increment value in m
h=0                     #Initial altitude 
slap=0                  #starting with initial slap

while h<=max_altitude:

    if h>=Height_Slaps[slap+1]:
        slap=slap+1
    
    Hb=Height_Slaps[slap]
    Pb=Pb_Slaps[slap]
    Tb=Tb_Slaps[slap]
    L=L_Slaps[slap]

    if L==0:
        p=Pb*math.exp((-1*g0*M*(h-Hb)/(R*Tb)))

    else:        
        bracket=(Tb+(L*(h-Hb)))/Tb
        exponent=(-1*g0*M)/(R*L)
        p=Pb*(bracket**exponent)

    hvals.append(h)
    pvals.append(p)

    h+=increment

for i in range(len(hvals)):
    print(hvals[i],pvals[i])
