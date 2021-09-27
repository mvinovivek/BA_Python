import random

x=1
while True:
    y=random.randint(1,100)
    with open("data.txt",'a') as testfile:
        testfile.write(str(x)+","+str(y)+"\n")
    x+=1
