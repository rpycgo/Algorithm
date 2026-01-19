import sys
import heapq


input = sys.stdin.readline


def dijkastra(
    N, grid,
    dx=[-1, 1, 0, 0],
    dy=[0, 0, -1, 1],
    ):
    dists = [[float('inf')] * (N+1) for _ in range(N+1)]
    dists[1][1] = grid[0][0]

    heap = [(grid[0][0], 1, 1)]
    while heap:
        curr_cost, curr_x, curr_y = heapq.heappop(heap)

        if dists[curr_x][curr_y] < curr_cost:
            continue

        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 1 <= nx <= N and 1 <= ny <= N:
                weight = grid[nx-1][ny-1]
                new_cost = curr_cost + weight

                if new_cost < dists[nx][ny]:
                    dists[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return dists


def main():
    i = 1
    while True:
        N = int(input())
        if N == 0:
            break

        grid = [
            list(map(int, input().split()))
            for _
            in range(N)
        ]

        dists = dijkastra(N, grid)
        answer = dists[N][N]
        print(f'Problem {i}: {answer}')

        i +=1


if __name__ == '__main__':
    main()
