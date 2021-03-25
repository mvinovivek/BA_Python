#we will some of the useful functions in the numpy library
import numpy as np

#Modifying the shape of the array
#to get the shape of array we can use shape function
a=np.arange(20)
print("Shape of a is",a.shape)

#to get the dimension of the array (usually 1d 2d kind)
print("Dimension of a is",a.ndim)


#to reshape an array we can use reshape function
b=a.reshape(4,5)
print(b)
print("Shape of b is", b.shape)
print("Dimension of b is", b.ndim)

c=a.reshape(2,2,5)
print(c)
print("Shape of c is", c.shape)
print("Dimension of c is", c.ndim)


#changing the value of an element in array
array=np.zeros(5)
print(array)

#Changing second element to 50
array[1]=50
print(array)

#changing value in 2d array
array=np.zeros((2,3))
print(array)

#Changing second element to 50
array[0,1]=50
array[1,2]=100
print(array)



#Math functions
#numpy by default supports most of the math functions in built 
#Element wise operations in numpy
numbers=np.arange(10)
five_times_numbers=numbers*5 #This will multiply every element in the array by 5
half_numbers=numbers/2       #This will divide every element in the array by 2
higher_numbers=numbers+10   #This will add 10 to every element in the array
lower_numbers=numbers-10    #This will subtract 10 from every element
squared_numbers=numbers**2  #This will square every element
cubed_numbers=numbers**3     #This will cube every number in the array

print(numbers)
print(five_times_numbers)
print(half_numbers)
print(higher_numbers)
print(lower_numbers)
print(squared_numbers)
print(cubed_numbers)


#Unary functions
negative_numbers=np.negative(numbers)
positive_numbers=np.positive(lower_numbers)

print(negative_numbers)
print(positive_numbers)

#lets start with trigonometric

#angles=np.arange(0,105,15)
angles=np.array((0,30,45,60,90))
radians=np.radians(angles)
sin_value=np.sin(radians)
cos_value=np.cos(radians)
tan_value=np.tan(radians)

print(angles)
print(radians)
print(sin_value)
print(cos_value)
print(tan_value)

#Rounding the values
print(np.round(angles,2))
print(np.round(radians,2))
print(np.round(sin_value,2))
print(np.round(cos_value,2))
print(np.round(tan_value,2))


#Using sum
a=np.random.randint(1,20,12).reshape(3,4)
print("Matrix is ")
print(a)
print("Sum along columns")
print(np.sum(a, axis=0))
print("Sum along rows")
print(np.sum(a,axis=1))
print("Sum of all elements")
print(np.sum(np.sum(a,axis=1),axis=0))


#Using sort
a=np.random.randint(1,100,12).reshape(3,4)
print("Matrix is ")
print(a)
print("Sorted along columns")
print(np.sort(a, axis=0))
print("Sort along rows")
print(np.sort(a,axis=1))