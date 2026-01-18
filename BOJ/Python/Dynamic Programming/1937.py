import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(r, c, n, grid, dp, dr, dc):
    if dp[r][c] != 0:
        return dp[r][c]

    dp[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] > grid[r][c]:
                max_dist = dfs(nr, nc, n, grid, dp, dr, dc) + 1
                dp[r][c] = max(dp[r][c], max_dist)

    return dp[r][c]


def main():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    n = int(input())
    grid = [
        list(map(int, input().split()))
        for _
        in range(n)
    ]

    dp = [[0] * n for _ in range(n)]

    answer = 0
    for r in range(n):
        for c in range(n):
            curr_dist = dfs(r, c, n, grid, dp, dr, dc)
            answer = max(answer, curr_dist)

    print(answer)


if __name__ == '__main__':
    main()
