import sys
from collections import deque


def get_external_air(
    N, M, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    visited = [[False] * M for _ in range(N)]

    queue = deque([(0, 0)])
    visited[0][0] = True

    to_melt = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    to_melt.append((nx, ny))

    return to_melt


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    time = 0
    last_cheese_count = 0

    while True:
        melt_list = get_external_air(N, M, grid)

        if not melt_list:
            break

        last_cheese_count = len(melt_list)

        for r, c in melt_list:
            grid[r][c] = 0

        time += 1

    print(time)
    print(last_cheese_count)


if __name__ == '__main__':
    main()
