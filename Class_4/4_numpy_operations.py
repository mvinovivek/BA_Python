#Here we will look at some other numpy operations
import numpy as np
from numpy.lib.twodim_base import tril

a=np.arange(12).reshape(3,4)
b=np.arange(12,24).reshape(3,4)

added=a+b   #Adding the two arrays, equivalent to np.add
difference=a-b 
multiply=a*b
divide=a/b 

print("Array a is")
print(a)
print("Array b is")
print(b)
print("Sum of a and b is")
print(added)
print("Difference between and b")
print(difference)
print("Element of a multiplied by b is")
print(multiply)
print("Divided value")
print(divide)

#Transposing the array
a=np.random.randint(10,100,6)
print(a, a.transpose())

a=np.random.randint(10,100,6).reshape(2,3)
print("Original Matrix")
print(a)
print("Transposed Matrix")
print(a.transpose())

print("Upper Matrix")
print(np.triu(a))

print("Lower Matrix")
print(np.tril(a))

#Linear algebra calculations
#Eigen values 
a=np.random.randint(1,100,9).reshape(3,3)
eigenvalues=np.linalg.eigvals(a)
print("Eigen values are")
print(eigenvalues)

#Dot product
a=np.arange(12).reshape(3,4)
b=np.arange(12,24).reshape(4,3)
dot_product=np.dot(a,b)
print("a Mutiplied by b is")
print(dot_product)


#Decomposing a matrix
# a=np.random.randint(1,100,16).reshape(4,4)
# decomposed=np.linalg.cholesky(a)
# print("Decomposed Matrix is")
# print(decomposed)

# #Matrix Divisions
# a=np.arange(16).reshape(4,4)
# b=np.arange(12,16).reshape(4)
# divided=np.linalg.solve(a,b)
# print(divided)