def main():
    N, K = map(int, input().split())

    dp = [[0] * (N+1) for _ in range(K+1)]

    for i in range(N+1):
        dp[1][i] = 1

    for k in range(2, K+1):
        for n in range(N+1):
            if n == 0:
                dp[k][n] = dp[k-1][n]
            else:
                dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1_000_000_000

    print(dp[K][N])


if __name__ == '__main__':
    main()
