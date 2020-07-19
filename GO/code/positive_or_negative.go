package main
import "fmt"

func main() {
	var num int
	fmt.Println("User, enter first number: ")
	fmt.Scan(&num)
	if (num >= 0) {
		fmt.Println(num, "is either zero or positive number")
	} else {
		fmt.Println(num, "is a negative number")
	}
}
