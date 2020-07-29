def string_to_array (strr, arr):
    strr = str(strr)
    lim = len(strr)
    for cnt in range(0, lim, 1):
        val = ord(strr[cnt])
        if (val >= 97 and val <= 122):
            val = int(val - 97)
        elif (val >=65 and val <= 90):
            val = int(val - 65)
        #print(str(val), end=",")
        arr.append(val)

def letter_histogram (arr):
    lim = len(arr)
    print("")
    for cnt in range(0, 26, 1):
        x = arr.count(cnt)
        if (x > 0):
            print(chr(cnt + 97), end=": (")
            perc = float(float(x*1.0 / lim)*100)
            print(str(perc) + "%)")

x = input("User, enter a string:\n")
x = str(x)
arr = []
string_to_array(x, arr)
letter_histogram(arr)
input("\nDONE!\n")
