import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            jump = grid[i][j]

            if dp[i][j] == 0 or (i==N-1 and j == N-1):
                continue

            if i + jump < N:
                dp[i+jump][j] += dp[i][j]

            if j + jump < N:
                dp[i][j + jump] += dp[i][j]

    answer = dp[N-1][N-1]

    print(answer)


if __name__ == '__main__':
    main()
