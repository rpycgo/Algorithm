import sys
import heapq


input = sys.stdin.readline


def main():
    n, m, k = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))

    dist = [[] for _ in range(n+1)]
    heapq.heappush(dist[1], 0)

    queue = [(0, 1)]
    while queue:
        cost, u = heapq.heappop(queue)

        for v, w in adj[u]:
            new_dist = cost + w

            if -dist[v][0] > new_dist:
                heapq.heappop(dist[v])

            heapq.heappush(dist[v], -new_dist)
            heapq.heappush(queue, (new_dist, v))

    for i in range(1, n+1):
        if len(dist[i]) < k:
            print(-1)
        else:
            print(-dist[i][0])


if __name__ == '__main__':
    main()
