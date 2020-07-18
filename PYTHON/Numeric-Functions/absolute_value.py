def absolute_value (num):
	num = int(num)
	if (num >= 0):
		return num
	else:
		return -num

x = int(input("User, enter a number: "))
results = absolute_value(x)
print("|" + str(x) + "| --> " + str(results))

