#this program demonstrate the simple function with arguments

def greet(name):                                #Function definition with argument
    print("Hi {}".format(name))
    print("Good Evening!")                  #code to be executed is intended


#greet()                         #Calling the function to make it run
greet("Bellatrix")                   #Directly passing the value

name="Bellatrix"
greet(name)                      #Passing a variable


#using the function with looping statements
names=["Ram", "Sita"]
for name in names:
    greet(name)



#Passing Multiple Arguments
def greet(name, message):
    print("Hi {}".format(name))
    print(message)

greet("Bellatrix", "You are Awesome!")