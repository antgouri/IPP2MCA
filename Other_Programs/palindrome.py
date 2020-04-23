val = input("Enter the string value\n")
print(end="\n")

rev = val[::-1]

if val == rev:
        print(val , "is a palindrome")
else:
        print(val , "is not a palindrome")
