#To print the output we can use the print funtion

print("This is my Output")

#we use print to variables also 

variable_1 = 10
variable_2 = "Vivek"
variable_3 = 60.0

print(variable_1)
print(variable_2)
print(variable_3)

#we can use print to show multiple outputs 
variable_1, variable_2, variable_3 = 10, "Vivek", 60.0
print(variable_1, variable_2, variable_3)

#There are some nice options
#print every variable in new linw
print(variable_1, variable_2, variable_3, sep="\n")

#print variables with tab space in between them
print(variable_1, variable_2, variable_3, sep="\t")

#print varibles with comma in between them
print(variable_1, variable_2, variable_3, sep=",")

#We can also use some ending values also
print(variable_1, variable_2, variable_3, sep="\n", end=";")

#We can use string formatting to mix variables and sentences
X = 10
Y = 20
print("Value of X is {} and Value of Y is {}".format(X, Y))

#Basic IO
name = input("Enter your name")
print("Hello {}!".format(name))

#we can also use srting addition
name = input("Enter your name")
print("Hello "+name+"!")
