import sys
import heapq


input = sys.stdin.readline


def dijkastra(start_node, n, adj):
    dists = [float('inf')] * (n+1)
    dists[start_node] = 0

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, weight in adj[curr_node]:
            new_cost = curr_cost + weight

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists


def main():
    n, m, r = map(int, input().split())
    n_items = [0] + list(map(int, input().split()))

    adj = [[] * (n+1) for _ in range(n+1)]
    for _ in range(r):
        u, v, w = map(int, input().split())

        adj[u].append((v, w))
        adj[v].append((u, w))

    max_items = float('-inf')
    for start_node in range(1, n+1):
        dists = dijkastra(start_node, n, adj)

        curr_total = 0
        for i in range(1, n+1):
            if dists[i] <= m:
                curr_total += n_items[i]

            if curr_total > max_items:
                max_items = curr_total

    print(max_items)


if __name__ == '__main__':
    main()
