import sys
from collections import deque


def main():
    input = sys.stdin.readline

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    T = int(input())
    for _ in range(T):
        l = int(input())
        start_x, start_y = map(int, input().split())
        end_x, end_y = map(int, input().split())

        grid = [[-1] * l for _ in range(l)]
        grid[start_x][start_y] = 0

        is_found = False

        queue = deque([(start_x, start_y)])
        while queue:
            x, y = queue.popleft()

            if x == end_x and y == end_y:
                is_found = True

                print(grid[x][y])
                break

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < l and 0 <= ny < l and grid[nx][ny] == -1:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))

        if not is_found:
            print(-1)


if __name__ == '__main__':
    main()
