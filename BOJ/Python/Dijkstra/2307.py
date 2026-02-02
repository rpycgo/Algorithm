import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, N, blocked_edge, parent, adj):
    dists = [float('inf')] * (N+1)
    dists[start_node] = 0

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            if (curr_node == blocked_edge[0] and next_node == blocked_edge[1]) or \
               (curr_node == blocked_edge[1] and next_node == blocked_edge[0]):
                continue

            new_cost = curr_cost + next_weight
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

                if blocked_edge == (0, 0):
                    parent[next_node] = curr_node

    return dists


def main():
    N, M = map(int, input().split())

    parent = [0] * (N+1)

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t = map(int, input().split())

        adj[a].append((b, t))
        adj[b].append((a, t))

    original_dists = dijkstra(1, N, (0, 0), parent, adj)

    path_edges = []
    curr_node = N
    while curr_node != 1:
        path_edges.append((parent[curr_node], curr_node))
        curr_node = parent[curr_node]

    max_delay = 0
    for edge in path_edges:
        delayed_dists = dijkstra(1, N, edge, parent, adj)

        if delayed_dists[N] == float('inf'):
            print(-1)
            return

        max_delay = max(max_delay, delayed_dists[N]-original_dists[N])

    print(max_delay)


if __name__ == '__main__':
    main()
