#Program to change cases using functions

def tolower(string):
 return string.lower()
 
def toupper(string):
 return string.upper()

def sswapcase(string):
 return string.swapcase()
 
def stitle(string):
 return string.title()
 
def caps(string):
 return string.capitalize()
 
def length(string):
 return len(string)
 
#Check the input methods..
#string = str(input("Enter the string value"))

#Hardcoded value
string = "The National Institute of Engineering, Mysuru"

print("ToLower", tolower(string))
print("ToUpper", toupper(string))
print("Tochangecase", sswapcase(string))
print("Title", stitle(string))
print("ToCaps", caps(string))
print("length", length(string))
