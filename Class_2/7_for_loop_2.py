#In case if we want to loop over several lists in one go, or need to access correspodnig 
#values of any list pairs, we can make use of the range method
# 
# range is a method when called will create an array of integers upto the given value
# for example range(3) will return an array with elements [0,1,2]

#now we can see that this is an array which can act as control variables
#Combining this with the len function, we can iterate over any number of lists

#Simple range example

numbers=[1,2,3,4,6,6,7,8,9,10]
squares=[]
cubes=[]

for number in numbers:
    squares.append(number**2)
    cubes.append(number**3)

for i in range(len(numbers)):
    print("The Square of {} is {}".format(numbers[i], squares[i]))
    
for i in range(len(numbers)):
    print("The Cube of {} is {}".format(numbers[i], cubes[i]))

#Finding sum of numbers upto a given number
number = 5
sum_value=0
for i in range(number + 1):
    sum_value = sum_value + i

print("The sum of numbers upto {} is {}".format(number,sum_value))

