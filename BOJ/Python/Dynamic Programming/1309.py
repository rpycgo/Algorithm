import sys


input = sys.stdin.readline


def main():
    MOD = 9901

    N = int(input())

    dp = [[0] * 3 for _ in range(N + 1)]
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1

    for i in range(1, N):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

    answer = sum(dp[N-1]) % MOD
    print(answer)


if __name__ == '__main__':
    main()
    