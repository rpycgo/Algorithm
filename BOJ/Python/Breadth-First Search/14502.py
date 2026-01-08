import sys
from collections import deque
from itertools import combinations


def main():
    def get_safe_area(current_matrix):
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        temp_matrix = [row.copy() for row in current_matrix]

        queue = deque(virus)
        while queue:
            y, x = queue.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < N and 0 <= nx < M:
                    if temp_matrix[ny][nx] == 0:
                        temp_matrix[ny][nx] = 2
                        queue.append((ny, nx))

        count = 0
        for row in temp_matrix:
            for col in row:
                if col == 0:
                    count += 1

        return count

    input = sys.stdin.readline

    N, M = map(int, input().split())

    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))

        matrix.append(row)

    empty = []
    virus = []
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == 0:
                empty.append((row, col))
            elif matrix[row][col] == 2:
                virus.append((row, col))

    ans = 0
    for walls in combinations(empty, 3):
        for ry, rx in walls:
            matrix[ry][rx] = 1

        ans = max(ans, get_safe_area(matrix))

        for ry, rx in walls:
            matrix[ry][rx] = 0

    print(ans)


if __name__ == '__main__':
    main()
