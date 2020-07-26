def binary_to_decimal (num):
	num = int(num)
	res = int(0)
	level = int(0)
	while (num > 0):
		temp = int(num % 10)
		temp = temp * pow(2, level)
		res = int(res + temp)
		level = int(level + 1)
		num = int(num / 10)
	return res

x = int(input("User, enter a BINARY number: "))
results = binary_to_decimal(x)
print(str(x) + " --> " + str(results))
