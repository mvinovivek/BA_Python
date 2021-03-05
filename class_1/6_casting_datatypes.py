#You can convert one data type to other by using the particular datatype keyword

float_var=52.6432
int_var=int(float_var)      #here we are converting float data type to int

int_var=5
float_var=float(int_var)    #here we are converting the float into int 

int_var=5
str_var=str(int_var)        #here we are converting the int into a str

#list can be converted into tuple and vice versa
list_1=[1,2,3,4,5,6,7]
tuple_1=tuple(list_1)

tuple_1=(1,2,3,4,5,6,7)
list_1=list(tuple_1)


#Why do we need this casting and what is its importance?
#By default in python, the input function will return the str data type
#But we cannot do mathematical operations with the str variable 
#So we need to cast either int or float over the input for doing math operations

raw_input=input("Enter a number")
print(type(raw_input))

#Best practice 
user_input=int(input("Enter a number"))
user_input=float(input("Enter a number"))
user_input=str(input("Enter a Name"))

#For fun, lets try one more
user_input=input("Enter a value")
int_var=int(user_input)
