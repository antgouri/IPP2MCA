n=int(input("Enter the number"))
fact=1
if n==0:
	print(fact)
else:
	for i in range(1,n+1):	
		fact*=i
print(fact)
