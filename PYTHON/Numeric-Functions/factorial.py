def factorial (num):
	num = int(num)
	res = int(1)
	while (num > 0):
		res = int(num * res)
		num = int(num - 1)
	return res

x = int(input("User, enter a number: "))
results = factorial(x)
print(str(x) + " --> " + str(results))
