#If statement in python is used to check whether a condition is true of false
#Based on the results of the conditions, one or other code will be executed. 
#Unlike other languages, python don't use any brackets to indicate the loop. 
#python works on indentation formatting. 
#the code to be placed inside should have one tab indented inside. 
#arbitrary space/indentation in python will throw  Indentation errors

#<------------------------------------------------>
#Simple if condition

X=10
if X>=15:
    print("X is greater than 15")

#The above code will not print anything as the value of X is less than 15. Try changing the value of the X higher than 15 and run!

#<------------------------------------------------>

#Simple if_else condition
age=15
if age>=18:
    print("You are eligible to Vote")

else:
    print("You are not eligible to Vote!")


#<---------------------------------------------->
#Another Example
number=15
if number%2==0:
    print("{} is even!".format(number))

else:
    print("{} is Odd!".format(number))

#<-------------------------------------------------->
#Nested If statements

number=50
if number>=100:
    print("The number entered is higher than 100!, Please enter value less than 100")

else:
    if number%2==0:
        print("{} is Even!".format(number))

    else:
        print("{} is Odd!".format(number))
    
#<---------------------------------------------------------->
#Elif statement

number = 3.4

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

#<---------------------------------------------------------->
#Elif statement example 2

number = 37

if number%2==0:
    print("The Number is divisible by 2")

elif number%3==0:
    print("The number is divisible by 3")

elif number%5==0:
    print("The number is divisible by 5")

else:
    print("The number is not divisible by 2,3,5")

#<-------------------------------------------------------->
#combining if with the logical operators
X = 10
if X >= 5 or X <= 5:
    print("This will alwasys be printed as it is in or")

if X >= 5 and X <= 5:
    print("This will never get printed as it is in and")

else:
    print("The above if loop will not get executed")