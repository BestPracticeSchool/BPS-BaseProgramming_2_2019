package main

import "fmt"

func add(a int, b int) int {
	return a + b
}

func empty() {
	fmt.Println("Hello")
}

func doubleVal(s int) (int, int) {
	square := s * s
	cube := s * s * s
	return square, cube
}

func sugar(a int) (temp int) {
	temp = a + 200
	return
}

func main() {
	fmt.Println()
	fmt.Println(add(2, 5))
	//var q int = 20
	empty()
	_, c := doubleVal(10)
	fmt.Println(c)

LOOP:
	for i := 0; i < 100; i++ {
		for j := 0; j < i; j++ {
			fmt.Println(i, j, i*j)

			if j > 25 {
				break LOOP
			}
		}
	}
}
