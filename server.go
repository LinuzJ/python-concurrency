package main

import (
	"fmt"
	"net/http"
)

func veryAdvancedCalculationsHandler(w http.ResponseWriter, r *http.Request) {
	var importantNumber = 500
	
	// Allocate big useless array
	uselessArray := make([][]int, importantNumber)
	for i := range uselessArray {
		uselessArray[i] = make([]int, importantNumber)
	}

	shameCount := 0

	// Do big expensive useless computation
	for i := 1; i < importantNumber; i++ {
		for j := 1; j < importantNumber; j ++ {
			if i + j % 2 == 0 {
				uselessArray[i][j] = i * j
			} else {
				// Loop of shame :(
				for k := 1; k < importantNumber * 10; k ++ {
					shameCount += i * j * k	
				}
			}
		}
	}

    fmt.Fprintf(w, "Sorry, I was doing very important calculations...")
}


func main() {
    http.HandleFunc("/", veryAdvancedCalculationsHandler)
    fmt.Println("Server started at :5000")
    http.ListenAndServe(":5000", nil)
}