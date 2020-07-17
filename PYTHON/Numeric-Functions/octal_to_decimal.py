def octal_to_decimal (num):
	num = int(num)
	res = int(0)
	level = int(0)
	while (num > 0):
		temp = int(num % 10)
		temp = int(temp * pow(8, level))
		res = int(res + temp)
		level = int(level + 1)
		num = int(num / 10)
	return res

def valid_octal (num):
	num = int(num)
	while (num > 0):
		temp = int(num % 10)
		if (temp == int(8) or temp == int(9)):
			return 0
		num = int(num / 10)
	return 1

x = int(input("User, enter an OCTAL number: "))
results = octal_to_decimal(x)
if (valid_octal(x) == int(1)):
	results = octal_to_decimal(x)
	print(str(x) + " --> " + str(results))
else:
	print("Entered number is NOT a valid octal number...")
