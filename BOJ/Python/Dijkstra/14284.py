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
            new_cost = curr_cost + next_weight

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists


def main():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())

        adj[a].append((b, c))
        adj[b].append((a, c))

    s, t = map(int, input().split())

    dists = dijkstra(s, n, adj)
    answer = dists[t]
    print(answer)


if __name__ == '__main__':
    main()
