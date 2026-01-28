import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, V, adj):
    dists = [float('inf')] * (V+1)
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
    V, E, P = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())

        adj[a].append((b, c))
        adj[b].append((a, c))

    dists_from_1 = dijkstra(1, V, adj)
    dists_from_P = dijkstra(P, V, adj)

    path_1_to_V = dists_from_1[V]
    path_1_to_P_to_V = dists_from_1[P] + dists_from_P[V]

    answer = 'SAVE HIM' if path_1_to_V == path_1_to_P_to_V else 'GOOD BYE'
    print(answer)


if __name__ == '__main__':
    main()
