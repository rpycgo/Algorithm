import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N = int(input())

    grid = []
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

        for j, num in enumerate(row):
            if num == 9:
                shark_x, shark_y = i, j
                grid[i][j] = 0

    time = 0
    eaten = 0
    shark_size = 2
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        queue = deque([(shark_x, shark_y, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[shark_x][shark_y] = True

        candidates = []
        min_distance = float('inf')

        while queue:
            x, y, distance = queue.popleft()

            if distance > min_distance:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and \
                      not visited[nx][ny] and grid[nx][ny] <= shark_size:
                    visited[nx][ny] = True

                    if 0 < grid[nx][ny] < shark_size:
                        candidates.append((distance+1, nx, ny))
                        min_distance = distance + 1
                    else:
                        queue.append((nx, ny, distance+1))

        if not candidates:
            break

        candidates.sort()
        distance, nx, ny = candidates[0]

        time += distance
        grid[nx][ny] = 0
        shark_x, shark_y = nx, ny
        eaten += 1

        if eaten == shark_size:
            shark_size += 1
            eaten = 0

    print(time)


if __name__ == '__main__':
    main()
