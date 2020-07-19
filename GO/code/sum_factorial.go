package main
import "fmt"

func main () {
	var num int
	res := 0
	fmt.Println("User, enter a number: ")
	fmt.Scan(&num)
	orig := num
	for (num > 0) {
		res += num
		num -= 1
	}
	fmt.Printf("%d --> %d\n", orig, res)
}
