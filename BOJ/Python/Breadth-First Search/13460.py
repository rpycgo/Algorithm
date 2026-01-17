import sys
from collections import deque


input = sys.stdin.readline


def move(x, y, grid, dx, dy):
    count = 0
    while grid[x + dx][y + dy] != '#' and grid[x][y] != 'O':
        x += dx
        y += dy

        count += 1

    return x, y, count


def main():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    N, M = map(int, input().split())

    grid = [
        list(input().rstrip())
        for _
        in range(N)
    ]

    rx, ry = 0, 0
    bx, by = 0, 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'R':
                rx, ry = r, c
            elif grid[r][c] == 'B':
                bx, by = r, c

    queue = deque([(rx, ry, bx, by, 1)])
    visited = [
        [
            [
                [False] * M
                for _
                in range(N)
            ]
            for _
            in range(M)
        ]
        for _
        in range(N)
    ]
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth > 10:
            break

        for i in range(4):
            nrx, nry, r_count = move(rx, ry, grid, dx[i], dy[i])
            nbx, nby, b_count = move(bx, by, grid, dx[i], dy[i])

            if grid[nbx][nby] == 'O':
                continue

            if grid[nrx][nry] == 'O':
                print(depth)
                return

            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth+1))

    print(-1)


if __name__ == '__main__':
    main()
