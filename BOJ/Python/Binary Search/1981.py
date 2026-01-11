import sys
from collections import deque


def bfs(n, board, low_limit, high_limit):
    if not (low_limit <= board[0][0] <= high_limit):
        return False

    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()

        if r == n - 1 and c == n - 1:
            return True

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if low_limit <= board[nr][nc] <= high_limit:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    return False


def main():
    input = sys.stdin.readline

    n = int(input())

    nums = set()
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))

        matrix.append(row)

        for start in row:
            nums.add(start)

    sorted_nums = sorted(list(nums))
    min_all, max_all = sorted_nums[0], sorted_nums[-1]

    low = 0
    high = max_all - min_all
    answer = high

    while low <= high:
        mid = (low+high) // 2

        possible = False
        for start in sorted_nums:
            end = start + mid

            if not (start <= matrix[n-1][n-1] <= end):
                continue

            if bfs(n, matrix, start, end):
                possible = True
                break

        if possible:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
