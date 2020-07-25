package main
import "fmt"

func between_ranges (lower int, upper int) {
	for lower <= upper {
		fmt.Printf("%d\n", lower)
		lower++
	}
}
func main () {
	var lwr int;
	var upr int;
	fmt.Println("User, enter the lower edge: ")
	fmt.Scan(&lwr)
	fmt.Println("User, enter the upper edge: ")
	fmt.Scan(&upr)
	between_ranges(lwr, upr)
}
