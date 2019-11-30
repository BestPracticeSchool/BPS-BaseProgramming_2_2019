package main

import "fmt"

func main() {
	fmt.Println("IFELSE CONDITOINS")
	if true && false {
		fmt.Println("Condition is true")
	} else if true && false {
		fmt.Println("Else if condition")
	} else {
		fmt.Println("Else block!")
	}

	if num := 10; num%2 == 0 {
		fmt.Println("Nums is ", num)

	}

	fmt.Println("############LOOPS IN GO##########")

	for i := 0; i <= 10; i += 3 { // C analog
		fmt.Println("Current i is: ", i)

	}
	j := 0
	for j <= 15 {
		fmt.Println("J current is :", j)
		j++
		if j > 20 {
			break
		}

	}

}
