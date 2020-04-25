# Content from: https://www.w3schools.com/python/python_strings.asp

#Array concept
a = "Hello, World!"
print(a[0])
print(a[1])

#Slicing concepts, positive index starts from 0th position
b = "Hello, World!"
print(b[2:5])
print(b[2:6])

#Slicing concepts, negative index starts from -1 position
b = "Hello, World!"
print(b[-5:-2])

#length method, remember does not work for int / float values. 
a = "Hello"
print(len(a))

#remove white spaces before / after
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Also recall uppper(), swapcase() methods
a = "Hello, World!"
print(a.lower())

#Replace at position...
a = "Hello, World!"
print(a.replace("H", "J"))

#split through a delimiter..
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String conctenation, to be careful with integer values..
a = "Hello"
b = "World"
c = a + b
print(c)

#string.format(), to watch the flower parentheses {}
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

