def solution(n: int, m: int) -> int:
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        dp[0][i] = i + 1

    if n >= 2:
        for i in range(1, n):
            for j in range(i, m):
                if i != j:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    return dp[n - 1][m - 1]


if __name__ == '__main__':
    n, m = map(int, input().split())

    print(solution(n, m))
