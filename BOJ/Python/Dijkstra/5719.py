import sys
import heapq
from collections import deque


input = sys.stdin.readline


def dijkstra(start_node, N, adj, removed):
    dists = [float('inf')] * N
    dists[start_node] = 0

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_cost in adj[curr_node]:
            if removed[curr_node][next_node]:
                continue

            new_cost = curr_cost + next_cost
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists


def remove_edge(d, s, dists, reverse_adj, removed):
    visited = [False] * len(dists)
    visited[d] = True

    queue = deque([d])
    while queue:
        curr_node = queue.popleft()

        if curr_node == s:
            continue

        for prev_node, prev_weight in reverse_adj[curr_node]:
            curr_cost = dists[prev_node] + prev_weight
            if curr_cost == dists[curr_node]:
                removed[prev_node][curr_node] = True

                if not visited[prev_node]:
                    visited[prev_node] = True
                    queue.append(prev_node)


def main():
    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            return

        s, d = map(int, input().split())

        reverse_adj = [[] for _ in range(N)]
        adj = [[] for _ in range(N)]
        for _ in range(M):
            u, v, p = map(int, input().split())

            adj[u].append((v, p))
            reverse_adj[v].append((u, p))

        removed = [[False] * N for _ in range(N)]

        dists = dijkstra(s, N, adj, removed)
        remove_edge(d, s, dists, reverse_adj, removed)
        dists_wo_edge = dijkstra(s, N, adj, removed)

        answer = dists_wo_edge[d] if dists_wo_edge[d] != float('inf') else -1
        print(answer)


if __name__ == '__main__':
    main()
