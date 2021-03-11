employee_1={
    'Emp_Code':'BA1004',
    'Name': 'Vivek',
    'Team': 'CSD'
}


print(employee_1['Name'])
print(employee_1['Team'])
print(employee_1['Emp_Code'])


#<------------------------------------------->
#More Practical Example

Copper={
    'Name':'Copper',
    'Density': 1000,
    'Conductivity' : 4544,
    'Yield Strength': 10e9,
}

SS={
    'Name':'Stainless Steel',
    'Density': 8000,
    'Conductivity' : 145,
    'Yield Strength': 14e9,
}


material=SS     #Material Selection
print("Density of {} is {} kg/m3".format(material['Name'], material['Density']))