print("Enter the first number:")
numFirst = int(input())
print("Enter the second number:")
numSce = int(input())
anz = numFirst * numSce
print(f"{numFirst} x {numSce} = {anz}")
if anz > 0:
	print("The result is positive.")
elif anz < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")
