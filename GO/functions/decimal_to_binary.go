package main
import "fmt"

func decimal_to_binary (num int) int {
	res := 0
	level := 1
	for (num > 0) {
		var tempI = num / 2
		var tempF = num*1.0 / 2
		fmt.Printf("tempI is %f\n", tempI)
		fmt.Printf("tempF is %f\n", tempF)
		res += tempF * level
		level *= 10
		num = tempI
	}
	return res
}

func main () {
	var x int
	var results int
	fmt.Println("User, enter an INTEGER: ")
	fmt.Scan(&x)
	results = decimal_to_binary(x)
	fmt.Printf("%d --> %d", x, results)
}
