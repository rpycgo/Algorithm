import sys
from collections import deque


input = sys.stdin.readline


def bfs(
    r, c, color,
    grid, visited, dr, dc,
    ):
    visited[r][c] = True
    group = [(r, c)]
    queue = deque([(r, c)])

    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < 12 and 0 <= nc < 6:
                if not visited[nr][nc] and grid[nr][nc] == color:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    group.append((nr, nc))

    return group if len(group) >= 4 else []


def arrange_blocks(grid):
    for c in range(6):
        temp = []

        for r in range(11, -1, -1):
            if grid[r][c] != '.':
                temp.append(grid[r][c])

        for r in range(12):
            grid[r][c] = '.'

        for i, val in enumerate(temp):
            grid[11-i][c] = val


def main():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    grid = [
        list(input().rstrip())
        for _
        in range(12)
    ]

    cnt = 0
    while True:
        visited = [[False] * 6 for _ in range(12)]
        to_pop = []

        for r in range(12):
            for c in range(6):
                if grid[r][c] != '.' and not visited[r][c]:
                    group = bfs(r, c, grid[r][c], grid, visited, dr, dc)

                    if group:
                        to_pop.extend(group)

        if not to_pop:
            break

        for r, c in to_pop:
            grid[r][c] = '.'

        cnt += 1

        arrange_blocks(grid)

    print(cnt)


if __name__ == '__main__':
    main()
