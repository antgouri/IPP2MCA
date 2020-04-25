name=input("Enter your name\n")

if len(name) >= 25:
 print("Invalid Name since ", name, "crosses the length condition with ", len(name), "characters")
else:
 print(name, " is valid")
 print(end='\n')
