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

def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		results = is_identical_digits(lower)
		if (results == int(1)):
			print(str(lower) + " has identical digits")
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))

between_ranges(lwr, upr)
