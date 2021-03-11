numbers=[1,2,3,4,6,6,7,8,9,10]
squares=[]
cubes=[]

for number in numbers:
    squares.append(number**2)
    cubes.append(number**3)

for i in range(len(numbers)):
    print("The Square of {} is {}".format(numbers[i],squares[i]))

for i in range(len(numbers)):
    print("The Cube of {} is {}".format(numbers[i],cubes[i]))