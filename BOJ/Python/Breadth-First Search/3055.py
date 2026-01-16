import sys
from collections import deque


def main():
    input = sys.stdin.readline

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    R, C = map(int, input().split())

    hedgehog_queue = deque()
    water_queue = deque()
    visited = [[False] * C for _ in range(R)]

    grid = []
    for i in range(R):
        row = list(input().rstrip())
        grid.append(row)

        for j, val in enumerate(row):
            if val == '*':
                water_queue.append((i, j))
            elif val == 'S':
                hedgehog_queue.append((i, j))
                visited[i][j] = True

    time = 0
    while hedgehog_queue:
        time += 1

        for _ in range(len(water_queue)):
            x, y = water_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == '.' or grid[nx][ny] == 'S':
                        grid[nx][ny] = '*'
                        water_queue.append((nx, ny))

        for _ in range(len(hedgehog_queue)):
            x, y = hedgehog_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 'D':
                        print(time)
                        return

                    if grid[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        hedgehog_queue.append((nx, ny))

    print('KAKTUS')


if __name__ == '__main__':
    main()
