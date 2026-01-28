import sys
import heapq


input = sys.stdin.readline


def dijkstra(
    start_r, start_c, target_r, target_c,
    N, M, grid,
    dr=(-1, 1, 0, 0),
    dc=(0, 0, -1, 1),
    ):
    dists = [[float('inf')] * M for _ in range(N)]
    dists[start_r][start_c] = 0

    heap = [(0, start_r, start_c)]
    while heap:
        curr_cost, curr_r, curr_c = heapq.heappop(heap)

        if dists[curr_r][curr_c] < curr_cost:
            continue

        if curr_r == target_r and curr_c == target_c:
            print(curr_cost)
            return

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                next_weight = 1 if grid[nr][nc] != '0' else 0
                new_cost = curr_cost + next_weight

                if new_cost < dists[nr][nc]:
                    dists[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))


def main():
    N, M = map(int, input().split())
    start_r, start_c, target_r, target_c = map(int, input().split())

    grid = [list(input().rstrip()) for _ in range(N)]

    dijkstra(start_r-1, start_c-1, target_r-1, target_c-1, N, M, grid)


if __name__ == '__main__':
    main()
