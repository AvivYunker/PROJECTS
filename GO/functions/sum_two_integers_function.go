package main
import "fmt"

func sum_two_ints(num1 int, num2 int) int {
	return num1 + num2
}

func main () {
	var n1 int
	var n2 int
	var res int
	fmt.Println("User, enter first number: ")
	fmt.Scan(&n1)
	fmt.Println("User, enter second number: ")
	fmt.Scan(&n2)
	res = sum_two_ints(n1, n2)
	fmt.Printf("%d + %d = %d\n", n1, n2, res)
}
