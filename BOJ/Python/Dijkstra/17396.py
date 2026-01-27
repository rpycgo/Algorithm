import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, N, adj, intersections):
    dists = [float('inf')] * N
    dists[start_node] = 0

    heap = [(0, start_node)]
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dists[curr_node] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            if next_node != N-1 and intersections[next_node] == 1:
                continue

            new_cost = curr_cost + next_weight

            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))

    return dists


def main():
    N, M = map(int, input().split())
    intersections = tuple(map(int, input().split()))

    adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())

        adj[a].append((b, t))
        adj[b].append((a, t))

    dists = dijkstra(0, N, adj, intersections)
    answer = dists[-1] if dists[-1] != float('inf') else -1
    print(answer)


if __name__ == '__main__':
    main()
