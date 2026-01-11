import sys
from collections import deque


def get_area_size(start_y, start_x, m, n, matrix):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    queue = deque([(start_y, start_x)])
    matrix[start_y][start_x] = 1
    size = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                size += 1
                queue.append((ny, nx))
    
    return size


def main():
    input = sys.stdin.readline

    M, N, K = map(int, input().split())

    matrix = [[0] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                matrix[y][x] = 1

    areas = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                area_size = get_area_size(i, j, M, N, matrix)
                areas.append(area_size)

    areas.sort()

    print(len(areas))
    print(*areas)


if __name__ == '__main__':
    main()
