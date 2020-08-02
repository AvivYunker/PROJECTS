def str_cat (str1, str2):
	res = str("")
	len1 = len(str1)
	len2 = len(str2)
	for i in range (0, len1, 1):
		res += str1[i]
	for j in range (0, len2, 1):
		res += str2[j]
	return res

str1 = input("User, enter first string: ")
str2 = input("User, enter second string: ")
results = str_cat(str1,str2)
print("results: " + str(results))
