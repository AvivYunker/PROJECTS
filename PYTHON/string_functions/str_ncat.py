def str_ncat (str1, str2, num):
	num = int(num)
	if (num > len(str2)):
		print("ERROR! number bigger than length of second string")
		return 0
	for i in range(0, num, 1):
		str1 += str2[i]
	return str1

str1 = input("User, enter the first string: ")
str2 = input("User, enter the second string: ")
num = int(input("User, enter the number: "))

results = str_ncat(str1, str2, num)
print("results: " + str(results))
