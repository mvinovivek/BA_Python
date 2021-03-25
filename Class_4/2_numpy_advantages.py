import numpy as np 
from timeit import default_timer as timer

def using_math(numbers):

    begin=timer()
    squared=[]
    for i in range(1,numbers):
        squared.append(i**2)
    end=timer()
    duration=end-begin

    return(duration)

def using_numpy(numbers):

    begin=timer()

    numbers=np.arange(1, numbers)
    squared=numbers**2

    end=timer()
    duration=end-begin

    return(duration)

print(using_math(100))
print(using_numpy(100))


#More details can be found here
#https://medium.com/swlh/why-use-numpy-d06c573fbcda