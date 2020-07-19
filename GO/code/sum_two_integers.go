package main
import "fmt"

func main() {
	var num1 int
	var num2 int
	fmt.Println("User, enter first number: ")
	fmt.Scan(&num1)
	fmt.Println("User, enter second number: ")
	fmt.Scan(&num2)
	fmt.Print("The sum of ", num1)
	fmt.Print(" and of ", num2)
	fmt.Println(" is:", (num1+num2))
}
