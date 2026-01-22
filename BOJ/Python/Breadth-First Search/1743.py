import sys
from collections import deque


input = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    N, M, K = map(int, input().split())

    grid = [[0] * (M+1) for _ in range(N+1)]
    for _ in range(K):
        r, c = map(int, input().split())
        grid[r][c] = 1

    visited = [[False] * (M+1) for _ in range(N+1)]

    max_size = float('-inf')
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                queue = deque([(i, j)])

                curr_size = 1
                while queue:
                    curr_x, curr_y = queue.popleft()

                    for k in range(4):
                        nx = curr_x + dx[k]
                        ny = curr_y + dy[k]

                        if 1 <= nx <= N and 1 <= ny <= M:
                            if grid[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                curr_size += 1
                                queue.append((nx, ny))

                if max_size < curr_size:
                    max_size = curr_size

    print(max_size)


if __name__ == '__main__':
    main()
