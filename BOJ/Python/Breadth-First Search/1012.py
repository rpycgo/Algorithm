import sys
from collections import deque


def bfs(matrix, start_y, start_x, n, m):
    dy = [-1 ,1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = deque([(start_y, start_x)])
    matrix[start_y][start_x] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 1:
                    matrix[ny][nx] = 0
                    queue.append((ny, nx))


def main():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())

        matrix = [[0] * M for _ in range(N)]

        for _ in range(K):
            x, y = map(int, input().split())
            matrix[y][x] = 1

        answer = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    bfs(matrix, i, j, N, M)
                    answer += 1

        print(answer)


if __name__ == '__main__':
    main()
