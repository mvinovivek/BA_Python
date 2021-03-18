#index errors will be raised when you try to access an index which is not present in the list or tuple or array

X=[1,2,3,4,5]
print(X[41])

#in case of dictionaries it will be KeyError
Person={
    'Name': 'Vivek',
    'Company' : 'Bellatrix'
}
print(Person['Name']) #it will work
print(Person['Age'])  #it will throw KeyError