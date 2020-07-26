def decimal_to_octal (num):
	num = int(num)
	res = int(0)
	level = int(1)
	while (num > 0):
		tempI = int(num / 8)
		tempF = float(num / 8.0)
		tempF = float(tempF - tempI)
		tempF = int(tempF * 8)
		res = int(res + tempF * level)
		level = int(level  * 10)
		num = int(tempI)
	return res

x = int(input("User, enter a number: "))
results = decimal_to_octal(x)
print(str(x) + " --> " + str(results))
