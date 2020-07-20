package main
import "fmt"

func factorial (num int) int  {
	res := 1
	var temp int
	for (num > 0) {
		temp = (num % 10)
		res = res * temp
		num -= 1
	}
	return res
}

func main () {
	var x int
	var results int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&x)
	results = factorial(x)
	fmt.Printf("%d --> %d\n", x, results)
}
