#This error will be raised when you try to open a file which is not available

file=open ('Test.txt', 'r') #File not found error

#Sometimes we may have the file in the folder but python cannot still open it. That maybe because of the path issue
#it is always better to give absolute path when opening file