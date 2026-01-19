import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, n, adj):
    dists = [float('inf')] * (n + 1)
    dists[start_node] = 0

    queue = [(0, start_node)]
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        if curr_cost < dists[curr_node]:
            continue

        for next_node, weight in adj[curr_node]:
            if curr_cost + weight < dists[next_node]:
                new_cost = curr_cost + weight
                dists[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

    return dists


def main():
    N = int(input())
    M = int(input())

    adj = [[] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    start_node, end_node = map(int, input().split())

    dists = dijkstra(start_node, N, adj)
    print(dists[end_node])


if __name__ == '__main__':
    main()
