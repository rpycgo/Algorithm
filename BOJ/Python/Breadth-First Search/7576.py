import sys
from collections import deque


def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())

    queue = deque()

    matrix = []
    for i in range(N):
        row = list(map(int, input().split()))

        matrix.append(row)
        for j in range(M):
            if row[j] == 1:
                queue.append((i, j))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = matrix[y][x] + 1
                    queue.append((ny, nx))

    max_days = 0
    for row in matrix:
        for tomato in row:
            if tomato == 0:
                print(-1)
                return

            max_days = max(max_days, tomato)

    answer = max_days - 1

    print(answer)


if __name__ == '__main__':
    main()
