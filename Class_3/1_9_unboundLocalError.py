#This will apply for function definitions where variable scope is applicable

#Global Scope
X=10
def func():
    print(X)

func()

#Local Scope
X=10
def func():
    X=5
    print("This is printing inside the function",X)
func()
print("This is printing outside the function",X)


#Unbound Local Error
X=10
def func():
    X=X+5
    print("This is printing inside the function",X)

func()
print("This is printing outside the function",X)

#Accessing global variable inside the function
X=10
def func():
    global X
    X=X+5
    print("This is printing inside the function",X)
func()
print("This is printing outside the function",X)