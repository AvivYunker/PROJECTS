def digit_counter (num):
	num = int(num)
	counter = int(0)
	if (num == int(0)):
		counter = int(1)
	else:
		while (num > 0):
			counter = int(counter + 1)
			num = int(num / 10)
	return counter

x = int(input("User, enter a number: "))
results = digit_counter(x)
print(str(x) + " has " + str(results) + " digits.")
