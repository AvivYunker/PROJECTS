def decimal_to_binary (num):
	num = int(num)
	level = int(1)
	res = int(0)
	while (num > 0):
		tempI = int(num / 2)
		tempF = float(num / 2.0)
		tempF = float(tempF - tempI)
		tempF = int(tempF * 2)
		res = int(res + tempF * level)
		level = int(level * 10)
		num = int(tempI)
	return res

def not_binary_array (arr_new, arr_old):
	for cnt in range(0, len(arr_old), 1):
		arr_new.append(1-int(arr_old[cnt]))

def digits_to_array (arr, num):
	num = int(num)
	while (num > 0):
		arr.append(num % 10)
		num = int(num / 10)


def array_to_number(num, arr):
	num = int(0)
	level = int(1)
	for cnt in range(0, len(arr), 1):
		num = int(num + arr[cnt]*level)
		level = int(level * 10)
	return num

def binary_to_decimal(num_d, num_b):
	num_b = int(num_b)
	level = int(0)
	while (num_b > 0):
		temp = int(num_b % 10)
		num_d = int(num_d + temp*pow(2,level))
		level = int(level + 1)
		num_b = int(num_b / 10)
	return num_d

x = int(input("User, enter a number: "))
bin_x = decimal_to_binary(x)
arr_x = []
arr_y = []
res_bin = int(0)
res_dec = int(0)
digits_to_array(arr_x, bin_x)
not_binary_array(arr_y, arr_x)
res_bin = array_to_number(res_bin, arr_y)
res_dec = binary_to_decimal(res_dec, res_bin)
print(str(x) + " --> " + str(res_dec))

