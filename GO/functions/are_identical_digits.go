package main
import "fmt"

func ident_digits (num int) int {
	dig := num % 10
	num /= 10
	for (num > 0) {
		if ((num % 10) != dig) {
			return 0
		}
	num /= 10
	}
return 1
}

func main () {
	var x int
	var results int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&x)
	results = ident_digits(x)
	if (results == 1) {
		fmt.Printf("%d HAS identical digits\n", x)
	}else {
		fmt.Printf("%d does NOT have identical digits\n", x)
	}
}
