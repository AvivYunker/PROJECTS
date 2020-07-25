def decimal_to_binary (num):
	num = int(num)
	res = int(0)
	level = int(1)
	while (num > 0):
		tempI = int(num / 2)
		tempF = float(num / 2.0)
		tempF = float(tempF - tempI)
		tempF = int(tempF * 2)
		res = int(res + tempF * level)
		level = int(level * 10)
		num = int(tempI)
	return res

def decimal_to_octal (num):
	num = int(num)
	res = int(0)
	level = int(1)
	while (num > 0):
		tempI = int(num / 8)
		tempF = float(num / 8.0)
		tempF = float(tempF - tempI)
		res = int(res + tempF * level)
		level = int(level * 10)
		num = int(tempI)
	return res

def decimal_to_hexadecimal (num):
	num = int(num)
	strr = str("")
	res = str("")
	while (num > 0):
		tempI = int(num / 16)
		tempF = float(num / 16.0)
		tempF = float(tempF - tempI)
		tempF = int(tempF * 16)
		num = int(tempI)
		if (tempF >= 0 and tempF <= 9):
			strr += str(tempF)
		elif (tempF >= 10 and tempF <= 16):
			strr += chr(tempF + 55)
	for cnt in range(len(strr)-1, -1, -1):
		res += str(strr[cnt])
	return res

def between_ranges(lower, upper):
	lower = int(lower)
	upper = int(upper)
	while (lower <= upper):
		decimal = int(lower)
		binary = int(decimal_to_binary(lower))
		octal = int(decimal_to_octal(lower))
		hexadecimal = str(decimal_to_hexadecimal(lower))
		print("DEC(" + str(decimal) + ") --> BIN(" + str(binary) + ") --> OCT(" + str(octal) + ") --> HEX(" + str(hexadecimal) + ")")
		lower = int(lower + 1)

lwr = int(input("User, enter the lower edge: "))
upr = int(input("User, enter the upper edge: "))
between_ranges(lwr, upr)
