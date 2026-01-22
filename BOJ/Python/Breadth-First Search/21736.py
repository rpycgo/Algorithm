import sys
from collections import deque


input = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    N, M = map(int, input().split())

    x_doyeon, y_doyeon = -1, -1

    grid = []
    for i in range(N):
        row = input().rstrip()
        grid.append(row)

        for j, col in enumerate(row):
            if col == 'I':
                x_doyeon, y_doyeon = i, j

    visited = [[False] * M for _ in range(N)]
    visited[x_doyeon][y_doyeon] = 1

    n_friends = 0
    queue = deque([(x_doyeon, y_doyeon)])

    while queue:
        curr_x, curr_y = queue.popleft()

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                    if grid[nx][ny] == 'P':
                        n_friends += 1

    answer = n_friends if n_friends else 'TT'
    print(answer)


if __name__ == '__main__':
    main()
