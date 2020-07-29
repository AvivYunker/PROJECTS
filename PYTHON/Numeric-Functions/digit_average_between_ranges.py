def digit_average (num):
	num = int(num)
	d = digit_counter(num)
	res = int(0)
	while (num > 0):
		res += int(num % 10)
		num = int(num / 10)
	res = float(res / d)
	return res

def digit_counter (num):
	counter = int(0)
	if (num == 0):
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
		print(str(lower) + " --> " + str(digit_average(lower)))
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
