def str_cpy (str1, str2):
	for i in range(0, len(str1), 1):
		str2 += str1[i]
	return str2

str1 = input("User, enter the first string: ")
str2 = str("")
str2 = str_cpy(str1, str2)
print("results are: " + str(str2))
