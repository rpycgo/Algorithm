import sys
from collections import deque


def get_external_air(N, M, grid, dx, dy):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return visited


def main():
    input = sys.stdin.readline

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    N, M = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    time = 0
    while True:
        external = get_external_air(N, M, grid, dx, dy)

        to_melt = []
        is_cheese_exist = False

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    is_cheese_exist = True

                    air_contact = 0
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]

                        if external[ni][nj]:
                            air_contact += 1

                    if air_contact >= 2:
                        to_melt.append((i, j))

        if not is_cheese_exist:
            break

        for r, c in to_melt:
            grid[r][c] = 0

        time += 1

    print(time)


if __name__ == '__main__':
    main()
