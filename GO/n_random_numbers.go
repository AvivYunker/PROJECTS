package main
import (
	"fmt"
	"math/rand"
)
func main () {
	var min int
	var max int
	fmt.Println("User, enter the lower edge: ")
	fmt.Scan(&min)
	fmt.Println("User, enter the max edge: ")
	fmt.Scan(&max)
	fmt.Printf("%d", (rand.Intn(max - min) + min))
}
