import sys
from collections import deque


input = sys.stdin.readline


def main():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    N = int(input())
    grid = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    island_idx = 1
    visited = [[False] * N for _ in range(N)]
    island_map = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                island_map[r][c] = island_idx

                queue = deque([(r, c)])
                while queue:
                    curr_r, curr_c = queue.popleft()

                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]

                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            island_map[nr][nc] = island_idx
                            queue.append((nr, nc))

                island_idx += 1

    dists = [[(-1, -1)] * N for _ in range(N)]

    queue = deque()
    for r in range(N):
        for c in range(N):
            if island_map[r][c] != 0:
                dists[r][c] = (island_map[r][c], 0)
                queue.append((r, c))

    min_bridge = float('inf')
    while queue:
        curr_r, curr_c = queue.popleft()
        curr_island, curr_dist = dists[curr_r][curr_c]

        if curr_dist > min_bridge:
            break

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if dists[nr][nc][0] == -1:
                    dists[nr][nc] = (curr_island, curr_dist+1)
                    queue.append((nr, nc))

                elif dists[nr][nc][0] != curr_island:
                    new_dist = dists[nr][nc][1] + curr_dist
                    if new_dist < min_bridge:
                        min_bridge = new_dist

    print(min_bridge)


if __name__ == '__main__':
    main()
