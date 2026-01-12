import sys
from collections import deque


def bfs(
    grid, visited,
    n, h, x, y,
    dx=[-1, 1, 0, 0], dy=[0, 0, -1, 1],
    ):
    visited[x][y] = True

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx, ny))


def main():
    input = sys.stdin.readline

    N = int(input())
    max_h = -1

    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))

        grid.append(row)

        for num in row:
            if max_h < num:
                max_h = num

    answer = 1
    for h in range(max_h):
        visited = [[False] * N for _ in range(N)]
        n_safe_areas = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] > h and not visited[i][j]:
                    bfs(grid, visited, N, h, i, j)
                    n_safe_areas += 1

        answer = max(answer, n_safe_areas)

    print(answer)


if __name__ == '__main__':
    main()
