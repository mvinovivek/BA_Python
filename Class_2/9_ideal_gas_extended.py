R_universal=8314.4626  #Universal Gas constant
MW=28.9647             #Molecular Weight of air
R = R_universal / MW  #Gas constant for the gas


pressure_values = []  #Empty array to hold all pressure values
temperature_values=[]  #Empty array to hold all the temperature values
rho_values=[]          #Empty array to hold all the density values
rho_triple=[]

initial_temp=350
final_temp=400
initial_press = int(10e5)
final_press = int(15e5)

#Populating the Temperature values
for i in range(initial_temp,final_temp):
    temperature_values.append(i)

#Populating the pressure values
for i in range(initial_press,final_press,int(1e5)):
    pressure_values.append(i)

#Finding the density for each temperature values
for pressure in pressure_values:
    for temperature in temperature_values:
        rho=pressure/(R*temperature)
        #print("The density of Air at {} bar pressure and {} K is {} kg/m3".format(pressure/1e5,temperature,rho))
        rho_values.append(rho)
        rho_triple.append([pressure,temperature,rho])
print(rho_values)

for i in range(len(rho_triple)):
    print(rho_triple[i])