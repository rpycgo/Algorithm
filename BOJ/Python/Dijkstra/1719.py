import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, n, adj):
    dists = [float('inf')] * (n+1)
    dists[start_node] = 0
    first_hop = ['-'] * (n+1)

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_cost in adj[curr_node]:
            new_cost = curr_cost + next_cost

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

                if curr_node == start_node:
                    first_hop[next_node] = next_node
                else:
                    first_hop[next_node] = first_hop[curr_node]

    return first_hop


def main():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())

        adj[u].append((v, w))
        adj[v].append((u, w))

    for i in range(1, n+1):
        result = dijkstra(i, n, adj)
        print(*result[1:])


if __name__ == '__main__':
    main()
