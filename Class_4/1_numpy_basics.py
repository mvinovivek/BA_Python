#We are importing numpy as np here. Now our namespace will be clear and we can always use np to access numpy function
import numpy as np

#arange function will arrange the numbers within the range with the given interval
#the first value is start value, second value is the stop value and the third value is the interval the values need to be arranged
aranged=np.arange(1,5)
print(aranged)

#with custom interval
aranged=np.arange(1.0,5.0,0.3)
print(aranged)

#From the previous function we can see that the numpy arranged the values for us. But there is a problem. Based on the interval the values in the end is not accurate.
#So we need to use a different function

#We can use the linspace function which will take the start value, end value, and number of divisions in between 
linearly_spaced=np.linspace(1.0,5.0,20)
print(linearly_spaced)

#to create an array of zeros 
zero_array=np.zeros(10)
print(zero_array)

#To create an array of ones
one_array=np.ones(10)
print(one_array)

#To create two dimensional arrays
#We can pass a tuple to create n dimensional arrays. In general first value is number of row and second value is number of columns
zeros_2d=np.zeros((10,2))
ones_2d=np.ones((10,2))
print(zeros_2d)
print(ones_2d)

#Converting numpy array to list
np_array=np.linspace(1.0,5.0,20)
print(type(np_array))
new_list=np_array.tolist()
print(new_list)
print(type(new_list))

#Converting a list or tuple into an np array
my_list=[1,2,3,4,5,6,7,8]
print(type(my_list))
my_array=np.array(my_list)
print(type(my_array))
print(my_array)

my_tuple=(1,2,3,4,5,6,7,8)
print(type(my_tuple))
my_tuple_array=np.array(my_tuple)
print(type(my_tuple_array))
print(my_tuple_array)

my_list=[1,2,3,4,5,6,7,8]
my_tuple=(8,7,6,5,4,3,2,1)
my_value=[my_list,my_tuple]
awesome_array=np.array(my_value)
print(awesome_array)

#To create a diagonal array
diagonal_array=np.diag([5,4,3])
print(diagonal_array)

#To extract diagonal of an array
X=np.arange(20).reshape(4,5)
print(X)
print(np.diag(X))