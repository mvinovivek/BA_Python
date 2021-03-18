# We can set some default values for the function arguments

#Passing Multiple Arguments
def greet(name, message="How are you!"):
    print("Hi {}".format(name))
    print(message)

greet("Bellatrix", "You are Awesome!")
greet("Bellatrix")

#NOTE Default arguments must come at the last. All arguments before default are called positional arguments
def greet(message="How are you!", name): #This will Throw error
    print("Hi {}".format(name))
    print(message)


#You can mix the positional values when using their name
#Passing Multiple Arguments
def greet(name, message):
    print("Hi {}".format(name))
    print(message)

greet( message="You are Awesome!",name="Bellatrix")