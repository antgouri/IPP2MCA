val = input("Enter the string value\n")
print(end="\n") 

rev = val[::-1] #Simplest method to reverse a string value. 

if val == rev:
        print(val , "is a palindrome")
else:
        print(val , "is not a palindrome")
