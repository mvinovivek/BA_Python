#For loop in the python is used to iterate over the items in a list or tuple. 
#for looping over the items we need to use the in keyword
#Like any other loops, the for loop also follows the intentation formatting. 
#Mutliple level of for loops can be created by multiple intentations

#<---------------------------->
#Simple example
fruits=['Apple', 'Orange', 'Mango', 'Banana']

for fruit in fruits:
    print("I like {}".format(fruit))

#<---------------------------------->
#Nested for loop
fruits=['Apple', 'Orange', 'Mango', 'Banana']
names=["Ram", "Sita"]
for name in names:
    for fruit in fruits:
        print("{} is eating {}".format(name,fruit))