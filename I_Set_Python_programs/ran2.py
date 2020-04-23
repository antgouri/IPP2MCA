'''
During class sessions, importance was given for random number generation with
random.random , random.randint and the range methods with significant details.
In fact, the difference in outputs were mentioned as well. 
'''
import random

print("The 3 odd random numbers within 100 and 200")
for i in range(3):
	print(random.randrange(101,200,2))

print("The 2 even random numbers within 10 and 40")
for i in range(2):
	print(random.randrange(10,40,2))


