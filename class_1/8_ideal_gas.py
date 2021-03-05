#In this code we will try to find the density of the gas for given pressure and temperature
#ideal gas equation is rho=P/RT

#Universal Gas Constant
R_universal=8314.4626

#Molecular weight of the gas
MW=28.9647

#Gas constant for the gas
R=R_universal/MW


#Pressure in Pascals
pressure=10e5

#Temperature in K
temperature = 350

rho=pressure/(R*temperature)

#Printing the Output
print("The density of Air at {} bar pressure and {} K is {} kg/m3".format(pressure/1e5,temperature,rho))