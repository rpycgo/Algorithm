// 1010
package main

import (
	"fmt"
)

func solution(n, m int) int {
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		dp[i][i] = 1
	}

	for j := 0; j < m; j++ {
		dp[0][j] = j + 1
	}

	if n >= 2 {
		for i := 1; i < n; i++ {
			for j := i; j < m; j++ {
				if i != j {
					dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
				}
			}
		}
	}

	return dp[n-1][m-1]
}

func main() {
	var T, N, M int

	fmt.Scanln(&T)

	for i := 0; i < T; i++ {
		fmt.Scanf("%d %d", &N, &M)
		fmt.Println(solution(N, M))
	}
}
