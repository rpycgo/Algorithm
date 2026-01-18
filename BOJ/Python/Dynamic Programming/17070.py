import sys


input = sys.stdin.readline


def main():
    N = int(input())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [
        [[0] * N for _ in range(N)]
        for _
        in range(3)
    ]
    dp[0][0][1] = 1

    for r in range(N):
        for c in range(1, N):
            if grid[r][c] == 1:
                continue

            if c-1 >= 0:
                dp[0][r][c] += (dp[0][r][c-1] + dp[2][r][c-1])

            if r-1 >= 0:
                dp[1][r][c] += (dp[1][r-1][c] + dp[2][r-1][c])

            if r-1 >= 0 and c-1 >= 0:
                if grid[r-1][c] == 0 and grid[r][c-1] == 0:
                    dp[2][r][c] += (dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1])

    answer = dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1]

    print(answer)


if __name__ == '__main__':
    main()
