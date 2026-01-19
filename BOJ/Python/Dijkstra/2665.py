import sys
import heapq


input = sys.stdin.readline


def dijkstra(
    n, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    dists = [[float('inf')] * (n) for _ in range(n)]
    dists[0][0] = 0

    heap = [(0, 0, 0)]
    while heap:
        curr_cost, curr_x, curr_y = heapq.heappop(heap)

        if dists[curr_x][curr_y] < curr_cost:
            continue

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                weight = 1 if grid[nx][ny] == '0' else 0
                new_cost = curr_cost + weight

                if new_cost < dists[nx][ny]:
                    dists[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return dists


def main():
    n = int(input())
    grid = [
        list(input().rstrip())
        for _
        in range(n)
    ]

    dists = dijkstra(n, grid)
    answer = dists[n-1][n-1]
    print(answer)


if __name__ == '__main__':
    main()
