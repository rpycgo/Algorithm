import sys
from collections import deque


def bfs(x, y, color, matrix, visited, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and matrix[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def get_area_count(n, matrix):
    visited = [[False] * n for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, matrix[i][j], matrix, visited, n)
                count += 1

    return count


def main():
    input = sys.stdin.readline

    N = int(input())
    matrix = [list(input().strip()) for _ in range(N)]

    n_normal = get_area_count(N, matrix)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'G':
                matrix[i][j] = 'R'

    n_blind = get_area_count(N, matrix)

    print(f'{n_normal} {n_blind}')


if __name__ == '__main__':
    main()
