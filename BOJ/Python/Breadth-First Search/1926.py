import sys
from collections import deque


def bfs(
    i, j, n, m, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    size = 1
    grid[i][j] = 0

    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                queue.append([nx, ny])

                size += 1

    return size


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _
        in range(n)
    ]

    n_pictures = 0
    max_size = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                n_pictures += 1

                size = bfs(i, j, n ,m ,grid)
                max_size = max(max_size, size)

    print(n_pictures)
    print(max_size)


if __name__ == '__main__':
    main()
