print("Enter a number less than 25")
Num = int(input())
if Num <= 25:
	for i in range(Num,26):
		print("Inside the loop, my variable is" + f"{i}")
else:
	print("Error")

