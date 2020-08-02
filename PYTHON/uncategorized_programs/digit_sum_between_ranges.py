def digit_sum (num):
	res = int(0)
	while (num > 0):
		temp = int(num % 10)
		res = int(res + temp)
		num = int(num / 10)
	return res

def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		res = digit_sum(lower)
		print(str(lower) + " --> " + str(res))
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
