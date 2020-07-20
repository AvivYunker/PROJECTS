def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		results = factorial(lower)
		print(str(lower) + " --> " + str(results))
		lower = int(lower + 1)

def factorial (num):
	num = int(num)
	res = int(1)
	while (num > 0):
		res = int(res * num)
		num = int(num - 1)
	return res

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
