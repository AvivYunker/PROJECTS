def digit_counter (num):
	num = int(num)
	counter = int(0)
	if (num == int(0)):
		counter = int(1)
	else:
		while (num > 0):
			counter = int(counter + 1)
			num = int(num / 10)
	return counter

def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		res = digit_counter(lower)
		print(str(lower) + " --> " + str(res))
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
