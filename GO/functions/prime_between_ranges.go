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

func between_ranges (lower int, upper int) {
	var results int
	for (lower <= upper) {
		results = is_prime(lower)
		if (results == 1) {
			fmt.Printf("%d is prime\n", lower)
		}
		lower += 1
	}
}

func main () {
	var lwr int
	var upr int
	fmt.Println("User, enter the lower edge: ")
	fmt.Scan(&lwr)
	fmt.Println("User, enter the upper edge: ")
	fmt.Scan(&upr)
	between_ranges(lwr, upr)
}
