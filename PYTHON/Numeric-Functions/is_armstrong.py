def is_armstrong (num):
	orig = int(num)
	num = int(num)
	d = digit_counter(num)
	sums = int(0)
	while (num > 0):
		temp = int(num % 10)
		temp = pow(temp, d)
		sums = int(sums + temp)
		num = int(num / 10)
	if (sums == orig):
		return 1
	else:
		return 0

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
results = is_armstrong(x)
if (results == int(1)):
	print(str(x) + " is an Armstrong")
else:
	print(str(x) + " is NOT an Armstrong")
