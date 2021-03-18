#unhandled code

X=10
Y=0
print(X/Y)
print("This is the end of Program!")

#Handled code
X=10
Y=0
try:
    print(X/Y)
except:
    print("Some error Occurred!")
print("This is the end of Program!")

#Handling with information code
X=10
Y=0
try:
    print(X/Y)
except Exception as e:
    print("Some error Occurred!")
    print(repr(e))
print("This is the end of Program!")