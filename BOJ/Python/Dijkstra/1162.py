import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, N, K, adj):
    dists = [[float('inf')] * (K+1) for _ in range(N+1)]
    dists[start_node][0] = 0

    heap = [(0, start_node, 0)]
    while heap:
        curr_cost, curr_node, curr_cnt = heapq.heappop(heap)

        if dists[curr_node][curr_cnt] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            new_cost = curr_cost + next_weight

            if new_cost < dists[next_node][curr_cnt]:
                dists[next_node][curr_cnt] = new_cost
                heapq.heappush(heap, (new_cost, next_node, curr_cnt))

            if curr_cnt < K and curr_cost < dists[next_node][curr_cnt+1]:
                dists[next_node][curr_cnt+1] = curr_cost
                heapq.heappush(heap, (curr_cost, next_node, curr_cnt+1))

    return dists


def main():
    N, M, K = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())

        adj[u].append((v, w))
        adj[v].append((u, w))

    dists = dijkstra(1, N, K, adj)
    answer = min(dists[N])
    print(answer)


if __name__ == '__main__':
    main()
