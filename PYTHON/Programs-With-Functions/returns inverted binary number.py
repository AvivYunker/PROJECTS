def binary_inverter (num):
    num = int(num)
    arrOrig = []
    arrInv = []
    digits_to_array(num, arrOrig)
    digit_inverter(arrOrig, arrInv)
    res = array_to_number(arrInv, num)
    return res

def digits_to_array (num, arrOrig):
    num = int(num)
    while (num > 0):
        temp = int(num % 10)
        arrOrig.append(temp)
        num = int(num / 10)
    lim = len(arrOrig)

def digit_inverter (arrOrig, arrInv):
    lim = len(arrOrig)
    for cnt in range(0, lim, 1):
        val = int(1 - arrOrig[cnt])
        arrInv.append(val)

def array_to_number (arrInv, num):
    num = int(0)
    lim = len(arrInv)
    level = int(1)
    for cnt in range(0, lim, 1):
        num = int(num + level * arrInv[cnt])
        level = int(level * 10)
    return num

x = input("User, enter a binary number:\n")
x = int(x)

results = binary_inverter(x)
print("Original: " + str(x))
print("Inverted: " + str(results))
input("\nDONE!\n")
