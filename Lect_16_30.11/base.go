package main

import "fmt"

var (
	name     = "Kek"
	lastName = "Lol"
	age      int
)

func main() {
	fmt.Println("Hello world!", 10, 20, 30) // print("Hello world")
	fmt.Println("I'm bob!")
	fmt.Printf("Hello %s\n", "James") // print("Hello %s\n", %("james"))

	/////VARIABLES AND TYPES
	var myVar int
	fmt.Println("Default value is : ", myVar)
	myVar = 25
	fmt.Println("My age is ", myVar)

	var myNewVar float64 = 27.123423453214
	fmt.Println("FLoat num is ", myNewVar)

	standAlone := 75423.324535
	fmt.Println("Stand Alone ", standAlone)

	myString := "Hello bob!"

	myBool := true || false && true

	fmt.Println(myString, myBool)
	fmt.Println(name, lastName)

	a, b := 20, 30
	fmt.Println(a, b)
	a, b = 20, 50
	fmt.Println(a, b)

}
