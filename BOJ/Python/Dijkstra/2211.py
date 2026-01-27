import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, N, adj):
    dists = [float('inf')] * (N+1)
    dists[start_node] = 0
    parents = [0] * (N + 1)

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            new_cost = curr_cost + next_weight

            if new_cost < dists[next_node]:
                parents[next_node] = curr_node
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists, parents


def main():
    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, C = map(int, input().split())

        adj[A].append((B, C))
        adj[B].append((A, C))

    _, parents = dijkstra(1, N, adj)
    print(N-1)
    for i in range(2, N+1):
        print(f'{i} {parents[i]}')


if __name__ == '__main__':
    main()
