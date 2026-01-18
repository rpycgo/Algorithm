import sys
from collections import deque


input = sys.stdin.readline


def calculate_n_icebergs(n, m, grid, icebergs, dx, dy):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for r, c in icebergs:
        if not visited[r][c]:
            count += 1

            if count>= 2:
                return 2

            queue = deque([(r, c)])
            visited[r][c] = True

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    return count


def main():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    N, M = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    icebergs = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] > 0:
                icebergs.append((r, c))

    years = 0
    while icebergs:
        count = calculate_n_icebergs(N, M, grid, icebergs, dx, dy)

        if count >= 2:
            print(years)
            return

        melt_list = []
        new_icebergs = []

        for r, c in icebergs:
            n_seas = 0

            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]

                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                    n_seas += 1

            melt_list.append((r, c, n_seas))

        for r, c, melt in melt_list:
            grid[r][c] = max(0, grid[r][c] - melt)

            if grid[r][c] > 0:
                new_icebergs.append((r, c))

        icebergs = new_icebergs
        years += 1

    print(0)


if __name__ == '__main__':
    main()
