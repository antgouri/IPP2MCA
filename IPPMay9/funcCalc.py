def add(a,b):
 return a+b

def sub(a,b):
 return a-b
 
def mul(a,b):
 return a*b
 
def div(a,b):
 return a/b

#Either read from std.keyboard or hardcode? 
num1=int(input("Enter A value"))
num2=int(input("Enter B value"))

print("1. Addition" , add(num1,num2))
print("2. Subtraction", sub(num1,num2))
print("3. Multiplication", mul(num1,num2))
print("4. Division", div(num1,num2))
