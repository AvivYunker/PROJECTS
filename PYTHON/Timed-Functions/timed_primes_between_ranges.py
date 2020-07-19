import timeit
def is_prime (num):
	num = int(num)
	b = (num - 1)
	while (b > 1):
		if (num % b == 0):
			return 0
		b = int(b - 1)
	return 1

def between_ranges (lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		results = is_prime(lower)
		if (results == int(1)):
			print(str(lower) + " is prime")
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))

start = timeit.default_timer()
between_ranges(lwr, upr)
finish = timeit.default_timer()
actual = finish - start
print("\nIt took: " + str(actual) + " seconds")

