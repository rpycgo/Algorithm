import sys
from collections import deque


input = sys.stdin.readline


def can_deliver(
    start_x, start_y, low_limit, high_limit,
    n_packages, N, grid, heights, dx, dy,
    ):
    if not (low_limit <= heights[start_x][start_y] <= high_limit):
        return False

    visited = [[False] * N for _ in range(N)]
    visited[start_x][start_y] = True
    n_delivered = 0

    queue = deque([(start_x, start_y)])
    while queue:
        curr_x, curr_y = queue.popleft()

        if grid[curr_x][curr_y] == 'K':
            n_delivered += 1

        if n_delivered == n_packages:
            return True

        for i in range(8):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if low_limit <= heights[nx][ny] <= high_limit:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return n_delivered == n_packages


def main():
    dx = (-1, 1, 0, 0, 1, 1, -1, -1)
    dy = (0, 0, -1, 1, 1, -1, 1, -1)

    N = int(input())

    n_packages = 0

    grid = []
    for i in range(N):
        row = input().rstrip()
        grid.append(row)

        for j, val in enumerate(row):
            if val == 'P':
                start_x, start_y = i, j
            elif val == 'K':
                n_packages += 1

    heights = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    heights_set = set()
    for x in range(N):
        for y in range(N):
            heights_set.add(heights[x][y])
    heights_list = sorted(list(heights_set))

    answer = float('inf')
    for low_limit in heights_list:
        if low_limit > heights[start_x][start_y]:
            break

        left = 0
        right = len(heights_list) - 1
        best_high = -1

        while left <= right:
            mid = (left + right) // 2
            high_limit = heights_list[mid]

            result = can_deliver(
                start_x, start_y, low_limit, high_limit,
                n_packages, N, grid, heights, dx, dy,
            )

            if result:
                best_high = high_limit
                right = mid -1
            else:
                left = mid + 1

        if best_high != -1:
            answer = min(answer, best_high - low_limit)

    print(answer)


if __name__ == '__main__':
    main()
