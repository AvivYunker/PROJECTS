def power(base, exponent):
	base = int(base)
	exponent = int(exponent)
	res = int(1)
	while (exponent > 0):
		res = int(res * base)
		exponent = int(exponent - 1)
	return res


x = int(input("User, enter the base: "))
y = int(input("User, enter the exponent: "))
results = power(x, y)
print(str(x) + "^" + str(y) + "=" + str(results))
