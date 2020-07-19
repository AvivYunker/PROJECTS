def is_identical_digits (num):
	num = int(num)
	dig = num % 10
	num = int(num / 10)
	while (num > 0):
		temp = int(num % 10)
		if (dig != temp):
			return 0
		num = int(num / 10)
	return 1

x = int(input("User, enter a number: "))
results = is_identical_digits(x)
if (results == int(1)):
	print(str(x) + " HAS identical digits.")
else:
	print(str(x) + " does NOT have identical digits.")
