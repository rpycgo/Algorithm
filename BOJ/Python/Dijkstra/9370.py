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

        for next_node, next_cost in adj[curr_node]:
            if curr_cost + next_cost < dists[next_node]:
                new_cost = curr_cost + next_cost

                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists


def main():
    T = int(input())
    for _ in range(T):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())

        gh_weight = 0

        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b, d = map(int, input().split())

            adj[a].append((b, d))
            adj[b].append((a, d))

            if (a == g and b == h) or (a == h and b == g):
                gh_weight = d

        candidates = [int(input()) for _ in range(t)]

        dist_s = dijkstra(s, n, adj)
        dist_g = dijkstra(g, n, adj)
        dist_h = dijkstra(h, n, adj)

        results = []
        for candidate in candidates:
            path1 = dist_s[g] + gh_weight + dist_h[candidate]
            path2 = dist_s[h] + gh_weight + dist_g[candidate]

            if dist_s[candidate] != float('inf'):
                if (path1 == dist_s[candidate]) or (path2 == dist_s[candidate]):
                    results.append(candidate)

        results.sort()
        print(*results)


if __name__ == '__main__':
    main()
