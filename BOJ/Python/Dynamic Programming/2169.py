import sys


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    grid = [
        tuple(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [[[float('-inf')] * 3 for _ in range(M)] for _ in range(N)]
    dp[0][0][0] = grid[0][0]
    for j in range(1, M):
        dp[0][j][1] = max(dp[0][j-1][0], dp[0][j-1][1]) + grid[0][j]

    for i in range(1, N):
        for j in range(M):
            prev_max = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2])
            dp[i][j][0] = prev_max + grid[i][j]

        for j in range(1, M):
            dp[i][j][1] = max(dp[i][j-1][0], dp[i][j-1][1]) + grid[i][j]

        for j in range(M-2, -1, -1):
            dp[i][j][2] = max(dp[i][j+1][0], dp[i][j+1][2]) + grid[i][j]

    answer = max(dp[N-1][M-1])
    print(answer)


if __name__ == '__main__':
    main()
