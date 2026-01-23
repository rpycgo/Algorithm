import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, n, adj):
    dists = [float('inf')] * (n+1)
    dists[start_node] = 0

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            next_cost = curr_cost + next_weight

            if next_cost < dists[next_node]:
                dists[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))

    return dists


def main():
    T = int(input())
    for _ in range(T):
        n, d, c = map(int, input().split())

        adj = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())

            adj[b].append((a, s))

        dists = dijkstra(c, n, adj)
        infected_dists = [dist for dist in dists if dist != float('inf')]

        print(f'{len(infected_dists)} {max(infected_dists)}')


if __name__ == '__main__':
    main()
