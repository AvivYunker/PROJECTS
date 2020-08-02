def str_cmp (str1, str2):
	str1, str2 = add_nulls(str1, str2)
	for cnt in range(0, len(str1), 1):
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
res = str_cmp(str1, str2)
print("results are: " + str(res))
