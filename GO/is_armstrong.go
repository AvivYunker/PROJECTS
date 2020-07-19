package main
import (
	"fmt"
	"math"
)

func digit_counter (num int) int {
	var counter int
	if (num == 0) {
		counter = 1
	} else {
		counter += 1
		num /= 10
	}
	return counter
}

func is_armstrong (num int) int {
	orig := num
	sums := 0
	d := digit_counter(num)
	var temp int
	for (num > 0) {
		temp = num % 10
		temp = math.Pow(temp, d)
		sums += temp
		num /= 10
	}
	if (sums == orig) {
		return 1
	} else {
		return 0
	}
}

func main () {
	var x int
	var results int
	fmt.Println("User, enter a number: ")
	fmt.Scan(&x)
	results = is_armstrong(x)
	if (results == 1) {
		fmt.Printf("%d IS an Armstrong", x)
	}else {
		fmt.Printf("%d is NOT an Armstrong", x)
	}
}
