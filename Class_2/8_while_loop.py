#while loop as the name suggest, will execute the code till the condition is true. 
#unlike for loop, while loop depends on the condition than looping over lists
#for every iteration of the loop, the control variable needs to be manually updated
#The user needs to be careful when defining while loop. if the control variable 
#is not updated properly, then there may be chances of infinite looping

x = 1
while x <= 10:
    print("This is iteration {}".format(x))
    x += 1  #same as x=x+1

#Example for infinite loop
x = 1
while x <= 10:
    print("This is iteration {}".format(x))
x += 1


#Common Example
error=1
while error >= 1e-8:
    #do calculation here
    pass
    