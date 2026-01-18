import sys


input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    grid = [
        list(map(int, list(input().rstrip())))
        for _
        in range(n)
    ]

    dp = [row[:] for row in grid]

    max_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_size = 1
                break

        if max_size == 1:
            break

    max_size = 0
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                max_size = max(max_size, dp[i][j])

    answer = max_size**2
    print(answer)


if __name__ == '__main__':
    main()
