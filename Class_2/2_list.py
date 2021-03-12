#A list in python is a datatype to hold data grouped togather. 
#list can contain any data value
#following are some of the handy options in a list 


list_1 = [1, 5, 7, 6, 17, 14, 21, 83]

#you can access particular value by using [] and index
print(list_1[2])  #it will print 7, as index starts at 0

#lists can also be sliced as in strings
print(list_1[:3])  #first four values
print(list_1[-4:])  #last four values
print(list_1[1:5])  #values from index 1 to index last
print(list_1[:-1])  #Omit the last value

#You can change the value of the list using the index
list_1[0] = 200
print(list_1)

list_1[1:2] = [500, 1000]
print(list_1)

#**len** will give len of the list 
print(len(list_1))

#**max** will give maximum value of the list and **min** will give minimum value of the list
list_1 = [1, 5, 7, 6, 17, 14, 21, 83]
print("The maximjum value is: {}".format(max(list_1)))
print("The minimum value is {}".format(min(list_1)))

#**insert** will insert the value at the given index
list_1 = [1, 5, 7, 6, 17, 14, 21, 83]
list_1.insert(1, "Inserted")
print(list_1)

#**append** will add the data to the last
list_1.append(456)
print(list_1)

#There is a catch here. Lets append a list 
list_1.append([2, 3])
print(list_1)

#we can see that it put that entire list at a single index. but we wanted the list to be
#extended. so we need to use the extend method
list_1 = [1, 5, 7, 6, 17, 14, 21, 83]
list_1.extend([2, 3])
print(list_1)

#extend will work with tuples also!
list_1 = [1, 5, 7, 6, 17, 14, 21, 83]
list_1.extend((2, 3))
print(list_1)

#**remove** will remove the value in the list, if the value is occuring in many places it will
#only remove the first valus
list_1.insert(1, "Inserted")
list_1.remove("Inserted")
print(list_1)

#**pop** will remove the values at the given index. if index is not given then it will delete 
#the last data
list_1.pop(2)
print(list_1)

list_1.pop()
print(list_1)

#**sort** will sort the values of the list in the ascending order
list_1.sort()
print(list_1)

#to make the sort in the descending order,we can use the reverse keyword
list_1.sort(reverse=True)
print(list_1)

#same as string we can use count to count the values
list_1 = [1, 5, 7, 6, 17, 14, 21, 83, 1]
print(list_1.count(1))

#**index** will give the index of the value
list_1 = [1, 5, 7, 6, 17, 14, 21, 83, 1]
print(list_1.index(21))


#Copying the lists are tricky
list_1 = [1, 5, 7, 6, 17, 14, 21, 82]
list_2 = list_1

list_2.append("Modified")
print(list_1, list_2)

#we can see both list got modified. to avoid this, we need to use copy method
list_1 = [1, 5, 7, 6, 17, 14, 21, 82]
list_2 = list_1.copy()

list_2.append("Modified")
print(list_1, list_2)