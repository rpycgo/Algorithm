import sys
from collections import deque


def bfs(
    start_y, start_x, h, w, grid,
    dy=[-1, 1, 0, 0, -1, -1, 1, 1],
    dx=[0, 0, -1, 1, -1, 1, -1, 1],
    ):
    queue = deque([(start_y, start_x)])
    grid[start_y][start_x] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 1:
                grid[ny][nx] = 0
                queue.append((ny, nx))


def main():
    input = sys.stdin.readline

    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        grid = [
            list(map(int, input().split()))
            for _
            in range(h)
        ]

        answer = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    bfs(i, j, h, w, grid)
                    answer += 1

        print(answer)


if __name__ == '__main__':
    main()
