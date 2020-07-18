import timeit
def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		results = is_armstrong(lower)
		if (results == int(1)):
			print(str(lower) + " is an Armstrong")
		lower = int(lower + 1)

def is_armstrong (num):
	orig = int(num)
	num = int(num)
	d = digit_counter(num)
	sums = int(0)
	while (num > 0):
		temp = int(num % 10)
		temp = pow(temp, d)
		sums = int(sums + temp)
		num = int(num / 10)
	if (sums == orig):
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


lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))

start = timeit.default_timer()
between_ranges(lwr, upr)
finish = timeit.default_timer()
actual = finish - start
print("\nIt took: " + str(actual) + " seconds")
