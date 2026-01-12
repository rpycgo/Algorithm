import sys
from collections import deque


def main():
    input = sys.stdin.readline

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    N, M = map(int, input().split())

    grid = [
        list(map(int, input().strip()))
        for _
        in range(N)
    ]

    visited = [
        [[0] * 2 for _ in range(M)]
        for _
        in range(N)
        ]
    visited[0][0][0] = 1

    queue = deque([(0, 0, 0)])
    while queue:
        x, y, broken = queue.popleft()

        if x == N-1 and y == M-1:
            print(visited[x][y][broken])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

    print(-1)


if __name__ == '__main__':
    main()
