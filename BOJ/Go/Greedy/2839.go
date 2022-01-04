// 2839
package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanln(&N)

	count := 0

	for N > 0 {
		if (N % 5) == 0 {
			count += (N / 5)
			N -= N
			break
		} else {
			N -= 3
			count++
		}
	}

	if (N == 0) && (count != 0) {
		fmt.Println(count)
	} else {
		fmt.Println(-1)
	}
}
