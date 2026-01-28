import sys
import heapq


def dijkstra(start_node, N, adj):
    dists = [float('inf')] * (N+1)
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
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        adj = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b, c = map(int, input().split())

            adj[a].append((b, c))
            adj[b].append((a, c))

        K = int(input())
        idx_friends = tuple(map(int, input().split()))

        dists = [0] * (N+1)
        for idx_friend in idx_friends:
            curr_dists = dijkstra(idx_friend, N, adj)

            for j in range(1, N+1):
                dists[j] += curr_dists[j]

        room_number_with_min_dist = -1
        min_dist = float('inf')

        for i in range(1, N+1):
            if dists[i] < min_dist:
                min_dist = dists[i]
                room_number_with_min_dist = i

        print(room_number_with_min_dist)


if __name__ == '__main__':
    main()
