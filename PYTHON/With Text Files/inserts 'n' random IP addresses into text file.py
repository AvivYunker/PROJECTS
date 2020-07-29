import random
def n_ip_addresses (num):
    num = int(num)
    strr = str("")
    while (num > 0):
        indv = int(4)
        while (indv > 0):
            rndm = random.randrange(0, 256)
            if (indv == 1):
                strr += str(rndm)
            else:
                strr += str(rndm)
                strr += str(".")
            indv = int(indv - 1)
            strr += str("")
        strr += str("\n")
        num = int(num - 1)
    return strr

def insert_to_txt (strr):
    strr = str(strr)
    file = open("n_random_IP.txt", "w")
    file.write(strr)
    file.close()


x = input("User, how many IP addresses?\n")
x = int(x)

str1 = n_ip_addresses(x)
insert_to_txt(str1)
input("\nDONE!\n")
