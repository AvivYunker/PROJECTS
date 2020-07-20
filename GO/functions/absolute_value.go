package main
import "fmt"

func absolute_value (num int) int {
	if (num >= 0) {
		return num
	} else {
		return -num
	}
}

func main () {
	var num int
	var results int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&num)
	results = absolute_value(num)
	fmt.Printf("|%d| --> %d\n", num, results)
}
