#Function can return a value 


#Defining the function
def cbrt(X):
    """
    This is called as docstring short form of Document String
    This is useful to give information about the function. 
    For example, 
    This function computes the cube root of the given number  
    """

    cuberoot=X**(1/3)

    return cuberoot         #This is returning value to the place where function is called

print(cbrt(27))

#calling using a variable
number=64
print("Cube root of {} is {}".format(number,cbrt(number)))

#Mentioning Type of the arguments
#Defining the function
def cbrt(X: float) -> float:
    cuberoot=X**(1/3)

    return cuberoot         #This is returning value to the place where function is called

print(cbrt(50))

#Mutiple returns
def calculation(X):
    sqrt=X**0.5
    cbrt=X**(1/3)

    return sqrt,cbrt

# print(calculation(9))
# values=calculation(9)
# print(values)

# values=calculation(9)
# print(values[0])

# sqrt,cbrt=calculation(9)
# print(sqrt,cbrt)