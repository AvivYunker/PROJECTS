def actual_radians (num):
	num = int(num)
	res = num % 360
	return res

x = int(input("User, enter radians: "))
results = actual_radians(x)
print(str(x) + " --> rad(" + str(results) + ")")

