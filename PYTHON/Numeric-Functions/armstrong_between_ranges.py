def between_ranges(lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		results = is_armstrong(lower)
		if (results == int(1)):
			print(str(lower))
		lower = int(lower + 1)

def is_armstrong (num):
	num = int(num)
	orig = int(num)
	sums = int(0)
	d = digit_counter(num)
	while (num > 0):
		temp = int(num % 10)
		temp = pow(temp, d)
		sums = int(sums + temp)
		num = int(num / 10)
	if (int(sums) == int(orig)):
		return 1
	else:
		return 0

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

lwr = input("User, enter the lower edge:\n")
upr = input("User, enter the upper edge:\n")

lwr = int(lwr)
upr = int(upr)

between_ranges(lwr, upr)

