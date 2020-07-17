def digit_sum (num):
	num = int(num)
	res = int(0)
	while (num > 0):
		temp = int(num % 10)
		res = int(res + temp)
		num = int(num / 10)
	return res

x = int(input("User, enter a number: "))
results = digit_sum(x)
print(str(x) + " --> " + str(results))
