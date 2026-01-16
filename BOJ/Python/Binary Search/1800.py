import sys
import heapq


input = sys.stdin.readline


def can_connect(limit, N, K, graph):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0

    heap = [(0, 1)]
    while heap:
        cost, curr = heapq.heappop(heap)

        if dist[curr] < cost:
            continue

        for neighbor, weight in graph[curr]:
            next_cost = cost + (1 if weight > limit else 0)

            if next_cost < dist[neighbor]:
                dist[neighbor] = next_cost
                heapq.heappush(heap, (next_cost, neighbor))

    return dist[N] <= K


def main():
    N, P, K = map(int, input().split())

    max_weight = 0
    graph = [[] for _ in range(N+1)]
    for _ in range(P):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

        max_weight = max(max_weight, w)

    left = 0
    right = max_weight

    answer = -1
    while left <= right:
        mid = (left + right) // 2

        if can_connect(mid, N, K, graph):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
