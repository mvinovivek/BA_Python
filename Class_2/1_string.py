#In this file the examples of various methods that can be use for a string is given

#**upper** will make all the characters into uppercase
string="hi! how are you?"
print(string.upper())

#**lower** will make all the characters into lowercase
string="HI! HOW ARE YOU!"
print(string.lower())

#**capitalize** will make the first letter of the string into uppercase and rest of the characters will be in lower case
string="hi! HOW are yoU?"
print(string.capitalize())

#**count** can be used to count the number of times the character is present in the string
string="hi! HOW are yoU?"
print(string.count("h"))

#**count** as default is case sensitive. A handy way to make it case insensitive is by making both string and the character to be counted into upper or lowercase
string="hi! HOW are yoU?"
print(string.upper().count("h".upper()))


#**replace** will replace the part of the string
string="hi! how are you?"
print(string.replace('h', 'A'))

#we can use the replace option to remove some unwanted characters also!
string="hi! how are you?"
print(string.replace("hi!",""))

#**split** will split the string with the given delimiter
string="hi! how are you?"
print(string.split('!'))

#Remember space is also delimiter!!!
string="hi! how are you?"
print(string.split(' '))

#Unfortunately by default the string cannot be split with multiple delimiters


#To find the len of the string, or to count the total characters in the string, we can use the len option
string="hi! how are you?"
print(len(string))

#Now to find the number of words in a given string, we can use the count method itself
string="hi! how are you?"
print(string.count(' ')+1)

#Spaces are the delimiters for words. A sentence with four words will have three spaces to it. Now this method will fail if the string has a space at the last!!

#string slicing
#we can slice a portion of string usign the [] brackets
string = "hi! how are you?"
print(string[2])        #Print the value at index 2
print(string[:3])       #print the values from index 0 to 3 (First four letters)
print(string[3:8])      #print letters from index 3 to 8
print(string[:-4])      #print everything except last four
print(string[-4:])      #print last four letters
