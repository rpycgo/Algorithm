import sys
import heapq


input = sys.stdin.readline


def dijkstra(start, n, adj):
    dists = [float('inf')] * (n + 1)
    dists[start] = 0

    queue = [(0, start)]
    while queue:
        dist, curr_node = heapq.heappop(queue)

        if dists[curr_node] < dist:
            continue

        for next_node, weight in adj[curr_node]:
            cost = dist + weight

            if cost < dists[next_node]:
                dists[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return dists


def main():
    N, E = map(int, input().split())

    adj = [[] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())

        adj[a].append((b, c))
        adj[b].append((a, c))

    v1, v2 = map(int, input().split())

    dist_from_1 = dijkstra(1, N, adj)
    dist_from_v1 = dijkstra(v1, N, adj)
    dist_from_v2 = dijkstra(v2, N, adj)

    path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
    path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]
    result = min(path1, path2)

    answer = -1 if result == float('inf') else result
    print(answer)


if __name__ == '__main__':
    main()
