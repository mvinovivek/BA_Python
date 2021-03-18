#Mutiple Error Handling code
X=10
Y=0
try:
    print(X/Y)
except ZeroDivisionError:
    print("Division by Zero is not supported!")

except TypeError:
    print("Division by String is not supported!")

print("This is the end of Program!")

#Mutiple Error Handling with tuples
X=10
Y=0
try:
    print(X/Y)
except (ZeroDivisionError, TypeError):
    print("Division by unsupported value")

print("This is the end of Program!")