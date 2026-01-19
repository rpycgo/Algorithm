import sys
import heapq


def dijkastra(start_node, d, adj):
    dists = [float('inf')] * (d + 1)
    dists[start_node] = 0

    queue = [(0, start_node)]
    while queue:
        curr_cost, curr_node = heapq.heappop(queue)

        if curr_cost > dists[curr_node]:
            continue

        for next_node, weight in adj[curr_node]:
            new_cost = curr_cost + weight

            if next_node <= d and new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))

    return dists


def main():
    N, D = map(int, input().split())

    adj = [[] * (D+1) for _ in range(D+1)]
    for i in range(D):
        adj[i].append((i+1, 1))

    for _ in range(N):
        u, v, w = map(int, input().split())

        if v <= D:
            adj[u].append((v, w))

    dists = dijkastra(0, D, adj)

    answer = dists[D]
    print(answer)


if __name__ == '__main__':
    main()
