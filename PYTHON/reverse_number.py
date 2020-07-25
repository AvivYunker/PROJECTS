def reverse_number(num):
	num = int(num)
	d = digit_counter(num)
	level = define_level(d)
	print("The 'd' is: " + str(d))
	print("The level is: " + str(level))
	res = int(0)
	while (num > 0):
		temp = int(num % 10)
		res = int(res + temp*level)
		level = int(level / 10)
		num = int(num / 10)
	return res

def digit_counter (num):
	num = int(num)
	counter = int(0)
	if (num == int(0)):
		counter = int(1)
	else:
		while (num > 0):
			num = int(num / 10)
			counter = int(counter + 1)
	return counter

def define_level(dig_cnt):
	dig_cnt = int(dig_cnt)
	res = int(1)
	while (dig_cnt > 1):
		res = int(res * 10)
		dig_cnt = int(dig_cnt - 1)
	return res

x = int(input("User, enter a number: "))
results = reverse_number(x)
print(str(x) + " --> " + str(results))
