import sys
import heapq


input = sys.stdin.readline


def dijkstra(
    start_r, start_c, h, w, grid,
    dr=(-1, 1, 0, 0),
    dc=(0, 0, -1, 1),
    ):
    dists = [[float('inf')] * (w+2) for _ in range(h+2)]
    dists[start_r][start_c] = 0

    heap = [(0, start_r, start_c)]
    while heap:
        curr_cost, curr_r, curr_c = heapq.heappop(heap)

        if dists[curr_r][curr_c] < curr_cost:
            continue

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < h+2 and 0 <= nc < w+2:
                if grid[nr][nc] == '*':
                    continue

                next_weight = 1 if grid[nr][nc] == '#' else 0
                new_cost = curr_cost + next_weight

                if new_cost < dists[nr][nc]:
                    dists[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    return dists


def main():
    T = int(input())
    for _ in range(T):
        h, w = map(int, input().split())

        grid = [['.'] * (w+2)]

        prisoners = []
        for i in range(1, h+1):
            row = list(''.join(['.', input().rstrip(), '.']))

            for j in range(w+2):
                if row[j] == '$':
                    prisoners.append((i, j))
            grid.append(row)
        grid.append(['.'] * (w+2))

        d0 = dijkstra(0, 0, h, w, grid)
        d1 = dijkstra(prisoners[0][0], prisoners[0][1], h, w, grid)
        d2 = dijkstra(prisoners[1][0], prisoners[1][1], h, w, grid)

        answer = float('inf')
        for i in range(h+2):
            for j in range(w+2):
                if d0[i][j] != float('inf') and d1[i][j] != float('inf') and d2[i][j] != float('inf'):
                    curr_cost = d0[i][j] + d1[i][j] + d2[i][j]

                    if grid[i][j] == '#':
                        curr_cost -= 2

                    answer = min(answer, curr_cost)

        print(answer)


if __name__ == '__main__':
    main()
