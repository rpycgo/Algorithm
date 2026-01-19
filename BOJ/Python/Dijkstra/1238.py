import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, n, adj):
    dists = [float('inf')] * (n + 1)
    dists[start_node] = 0

    queue = [(0, start_node)]
    while queue:
        dist, curr_node = heapq.heappop(queue)

        if dists[curr_node] < dist:
            continue

        for next_node, weight in adj[curr_node]:
            cost = dist + weight

            if cost < dists[next_node]:
                dists[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return dists


def main():
    N, M, X = map(int, input().split())

    adj = [[] * (N+1) for _ in range(N + 1)]
    reverse_adj = [[] * (N+1) for _ in range(N + 1)]
    for _ in range(M):
        u, v, t = map(int, input().split())

        adj[u].append((v, t))
        reverse_adj[v].append((u, t))

    dists_go = dijkstra(X, N, adj)
    dists_comback = dijkstra(X, N, reverse_adj)

    max_time = 0
    for i in range(1, N+1):
        total = dists_go[i] + dists_comback[i]

        if total != float('inf'):
            if total > max_time:
                max_time = total

    print(max_time)


if __name__ == '__main__':
    main()
