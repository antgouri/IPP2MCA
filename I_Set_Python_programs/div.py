num = int(input())
den = int(input())

try:
	quo = num / den
	print(quo)
except:
	if den == 0:
		print("Denominator should not be 0")
	

