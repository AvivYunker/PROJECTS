package main
import "fmt"

func main() {
	var num int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&num)
	if (num > 0) {
		fmt.Println("The number is positive")
	} else if (num == 0) {
		fmt.Println("The number is zero")
	} else {
		fmt.Println("The number is negative")
	}
}
