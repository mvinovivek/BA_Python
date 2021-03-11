R_universal=8314.4626  #Universal Gas constant
MW=28.9647             #Molecular Weight of air
R=R_universal/MW       #Gas constant for the gas
pressure=10e5          #Pressure in Pascals

temperature_values=[]  #Empty array to hold all the temperature values
rho_values=[]          #Empty array to hold all the density values
intial_value=350
final_value=400

#Populating the Temperature values
for i in range(intial_value,final_value):
    temperature_values.append(i)

#Finding the density for each temperature values
for temperature in temperature_values:
    rho=pressure/(R*temperature)
    print("The density of Air at {} bar pressure and {} K is {} kg/m3".format(pressure/1e5,temperature,rho))
    rho_values.append(rho)
    
print(rho_values)