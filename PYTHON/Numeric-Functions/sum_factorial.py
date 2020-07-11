def sum_factorial (num):
	num = int(num)
	res = int(0)
	while (num > 0):
		res = int(res + num)
		num = int(num - 1)
	return res

x = int(input("User, enter a number: "))
results = sum_factorial(x)
print(str(x) + " --> " + str(results))
