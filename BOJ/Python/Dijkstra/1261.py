import sys
import heapq


input = sys.stdin.readline


def dijkastra(
    N, M, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    dists = [[float('inf')] * (M + 1) for _ in range(N+1)]
    dists[1][1] = 0

    heap = [(0, 1, 1)]
    while heap:
        curr_cost, curr_x, curr_y = heapq.heappop(heap)

        if dists[curr_x][curr_y] < curr_cost:
            continue

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 1 <= nx <= N and 1 <= ny <= M:
                weight = 1 if grid[nx-1][ny-1] == 1 else 0
                new_cost = curr_cost + weight

                if new_cost < dists[nx][ny]:
                    dists[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return dists


def main():
    M, N = map(int, input().split())

    grid = [
        list(map(int, input().rstrip()))
        for _
        in range(N)
    ]

    dists = dijkastra(N, M, grid)
    answer = dists[N][M]
    print(answer)


if __name__ == '__main__':
    main()
