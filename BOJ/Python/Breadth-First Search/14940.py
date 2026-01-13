import sys
from collections import deque


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    start_x = -1
    start_y = -1

    answer = [[-1]*m for _ in range(n)]

    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

        for j, val in enumerate(row):
            if val == 2:
                answer[i][j] = 0

                start_x = i
                start_y = j
            elif val == 0:
                answer[i][j] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and answer[nx][ny] == -1:
                answer[nx][ny] = answer[x][y] + 1
                queue.append((nx, ny))

    for row in answer:
        print(*row)


if __name__ == '__main__':
    main()
