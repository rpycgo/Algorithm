import sys
from collections import deque


input = sys.stdin.readline


def main():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    N, M = map(int, input().split())
    grid = [
        list(input().rstrip())
        for _
        in range(N)
    ]

    start_r, start_c = 0, 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == '0':
                start_r, start_c = r, c
                grid[r][c] = '.'

    visited = [[[False] * 64 for _ in range(M)] for _ in range(N)]
    visited[start_r][start_c][0] = True

    queue = deque([(start_r, start_c, 0, 0)])
    while queue:
        curr_r, curr_c, keys, dist = queue.popleft()

        if grid[curr_r][curr_c] == '1':
            print(dist)
            return

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != '#':
                cell = grid[nr][nc]

                if 'a' <= cell <= 'f':
                    nk = keys | (1 << (ord(cell) - ord('a')))
                    if not visited[nr][nc][nk]:
                        visited[nr][nc][nk] = True
                        queue.append((nr, nc, nk, dist+1))
                elif 'A' <= cell <= 'F':
                    if keys & (1 << (ord(cell) - ord('A'))):
                        if not visited[nr][nc][keys]:
                            visited[nr][nc][keys] = True
                            queue.append((nr, nc, keys, dist+1))
                else:
                    if not visited[nr][nc][keys]:
                        visited[nr][nc][keys] = True
                        queue.append((nr, nc, keys, dist+1))

    print(-1)


if __name__ == '__main__':
    main()
