def digit_average (num):
	num = int(num)
	d = digit_counter(num)
	res = int(0)
	while (num > 0):
		res += int(num % 10)
		num = int(num / 10)
	res = float(res / d)
	return res

def digit_counter (num):
	counter = int(0)
	if (num == 0):
		counter = int(1)
	else:
		while (num > 0):
			counter = int(counter + 1)
			num = int(num / 10)
	return counter

x = int(input("User, enter a number: "))
results = digit_average(x)
print(str(x) + " --> " + str(results))
