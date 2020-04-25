#Program to check for voting eligibility. 

name=input("Enter your name\n")
age=int(input("Enter your age\n"))

#a dummy condition for the after age
if age >= 18 and age < 95:
 print(name, "is eligible for voting", "with ", age, "years")
else:
 print("Not eligible for voting")
