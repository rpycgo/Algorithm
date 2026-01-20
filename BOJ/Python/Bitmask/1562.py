import sys


input = sys.stdin.readline


def main():
    MOD = 10**9

    N = int(input())

    dp = [
        [
            [0] * 1024 for _ in range(10)
        ]
        for _ in range(N + 1)
    ]

    for j in range(1, 10):
        dp[1][j][1 << j] = 1

    for i in range(1, N):
        for j in range(10):
            for visit in range(1024):
                if dp[i][j][visit] == 0:
                    continue

                if j > 0:
                    next_visit = visit | (1 << (j-1))
                    dp[i+1][j-1][next_visit] = (dp[i+1][j-1][next_visit] + dp[i][j][visit]) % MOD

                if j < 9:
                    next_visit = visit | (1 << (j+1))
                    dp[i+1][j+1][next_visit] = (dp[i+1][j+1][next_visit] + dp[i][j][visit]) % MOD

    answer = 0
    for j in range(10):
        answer = (answer + dp[N][j][1023]) % MOD

    print(answer)


if __name__ == '__main__':
    main()
