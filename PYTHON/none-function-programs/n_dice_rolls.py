import random
def main():
	x = int(input("User, how many random numbers? "))
	while (x > 0):
		rndm = random.randrange(1,7)
		print(str(rndm), end=",")
		x = int(x - 1)
	print("")
main()
