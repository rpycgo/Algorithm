import sys
from collections import deque


def bfs(
    i, j, N, M, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    visited = [[-1] * M for _ in range(N)]
    visited[i][j] = 0

    distance = 0

    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == -1 and grid[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                    distance = max(distance, visited[nx][ny])

    return distance


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    grid = [
        list(input().rstrip())
        for _
        in range(N)
    ]

    max_distance = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'L':
                distance = bfs(i, j, N, M, grid)

                max_distance = max(max_distance, distance)

    print(max_distance)


if __name__ == '__main__':
    main()
