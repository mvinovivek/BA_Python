#Python allows arbitrary number of variables 

def summation(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    
    return  sum 


print(summation(1))
print(summation(1,2))
print(summation(1,2,3))
print(summation(1,2,3,4))
print(summation(1,2,3,4,5))


#Mixing Positional, Default and arbitrary

def awesomeFunction(name,*messages,greet="Greetings"):
    print("Hi {}".format(name))
    print(greet)
   
    if len(messages)==0:
        print("You have no new messages")
    
    else:
        print("Your Messages are!")
        for message in messages:
            print(message)

awesomeFunction("Vivek")
awesomeFunction("Vivek", "Message 1")
awesomeFunction("Vivek", "Message 1","Message 2")
awesomeFunction("Vivek", "Message 1", "Message 2", "Message 3", greet="Good Morning!")