def str_ncmp (str1, str2, num):
	num = int(num)
	str1, str2 = add_nulls(str1, str2)
	#print("Length of str1: " + str(len(str1)))
	#print("Length of str2: " + str(len(str2)))
	if (num > len(str1)):
		print("ERROR! number bigger than string length")
		return 0
	else:
		for cnt in range(0, num, 1):
			if (ord(str1[cnt]) > ord(str2[cnt])):
				return 1
			elif (ord(str1[cnt]) < ord(str2[cnt])):
				return -1
		return 0

def add_nulls (str1, str2):
	while (len(str1) < len(str2)):
		str1 += '\0'
	while (len(str2) < len(str1)):
		str2 += '\0'
	return str1, str2

str1 = input("User, enter the first string: ")
str2 = input("User, enter the second string: ")
num = int(input("User, enter the number: "))

res = str_ncmp(str1, str2, num)
print("Results: " + str(res))
