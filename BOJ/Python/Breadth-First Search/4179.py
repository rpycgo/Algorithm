import sys
from collections import deque


input = sys.stdin.readline


def main():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    R, C = map(int, input().split())
    grid = [
        list(input().rstrip())
        for _
        in range(R)
    ]

    fire_dists = [[-1] * C for _ in range(R)]
    jihoon_dists = [[-1] * C for _ in range(R)]

    fire_queue = deque()
    jihoon_queue = deque()

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'J':
                jihoon_dists[r][c] = 0
                jihoon_queue.append((r, c))
            elif grid[r][c] == 'F':
                fire_dists[r][c] = 0
                fire_queue.append((r, c))

    while fire_queue:
        curr_r, curr_c = fire_queue.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] != '#' and fire_dists[nr][nc] == -1:
                    fire_dists[nr][nc] = fire_dists[curr_r][curr_c] + 1
                    fire_queue.append((nr, nc))

    while jihoon_queue:
        curr_r, curr_c = jihoon_queue.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                print(jihoon_dists[curr_r][curr_c] + 1)
                return

            if grid[nr][nc] == '.' and jihoon_dists[nr][nc] == -1:
                if fire_dists[nr][nc] == -1 or jihoon_dists[curr_r][curr_c] + 1 < fire_dists[nr][nc]:
                    jihoon_dists[nr][nc] = jihoon_dists[curr_r][curr_c] + 1
                    jihoon_queue.append((nr, nc))

    print('IMPOSSIBLE')


if __name__ == '__main__':
    main()
