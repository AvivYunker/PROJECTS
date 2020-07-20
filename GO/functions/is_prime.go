package main
import "fmt"

func is_prime (num int) int {
	b := num - 1
	for (b > 1) {
		if (num % b == 0) {
			return 0
		}
	b -= 1
	}
return 1
}

func main () {
	var x int
	var results int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&x)
	results = is_prime(x)
	if (results == 1) {
		fmt.Printf("%d IS a prime\n", x)
	} else {
	fmt.Printf("%d is NOT a prime\n", x)
	}
}
