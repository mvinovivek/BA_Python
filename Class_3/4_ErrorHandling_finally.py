#Error Handling with finally
X=10
Y=2
try:
    print(X/Y)
except ZeroDivisionError:
    print("Division by Zero is not supported!")

except TypeError:
    print("Division by String is not supported!")

finally:
    print("This will always be executed!")

print("This is the end of Program!")