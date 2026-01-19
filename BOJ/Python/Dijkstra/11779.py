import sys
import heapq


input = sys.stdin.readline


def dijkastra(start_node, n, adj):
    dists = [float('inf')] * (n+1)
    dists[start_node] = 0

    parent = [0] * (n+1)

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

                parent[next_node] = curr_node

    return dists, parent


def main():
    n = int(input())
    m = int(input())

    adj = [[] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())

        adj[u].append((v, w))

    start_node, end_node = map(int, input().split())

    dists, parent = dijkastra(start_node, n, adj)

    path = []
    curr_node = end_node
    while curr_node != 0:
        path.append(curr_node)
        curr_node = parent[curr_node]
    path.reverse()

    min_cost = dists[end_node]
    n_cities = len(path)

    print(min_cost)
    print(n_cities)
    print(*path)


if __name__ == '__main__':
    main()
