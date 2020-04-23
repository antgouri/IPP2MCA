import math

num = int(input("Enter the number to count the number of digits"))

numOfDig=math.floor(math.log10(num))+1

print(numOfDig)

print(type(numOfDig))


