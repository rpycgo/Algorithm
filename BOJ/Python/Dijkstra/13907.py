import sys
import heapq


input = sys.stdin.readline


def apply_tax(curr_tax, candidates):
    result = float('inf')
    for cnt, weight in candidates:
        result = min(result, weight + cnt*curr_tax)

    return result


def dijkstra(start_node, N, adj):
    dists = [[float('inf')] * N for _ in range(N+1)]
    dists[start_node][0] = 0

    heap = [(0, start_node, 0)]
    while heap:
        curr_cost, curr_node, cnt = heapq.heappop(heap)

        skip = False
        for i in range(cnt):
            if dists[curr_node][i] <= curr_cost:
                skip = True
                break

        if skip:
            continue

        if dists[curr_node][cnt] < curr_cost or cnt >= N-1:
            continue

        for next_node, next_weight in adj[curr_node]:
            new_cost = curr_cost + next_weight

            if new_cost < dists[next_node][cnt+1]:
                dists[next_node][cnt+1] = new_cost
                heapq.heappush(heap, (new_cost, next_node, cnt+1))

    return dists


def main():
    N, M, K = map(int, input().split())
    S, D = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, w = map(int, input().split())

        adj[a].append([b, w])
        adj[b].append([a, w])

    dists = dijkstra(S, N, adj)

    candidates = [
        (cnt, dists[D][cnt])
        for cnt
        in range(1, N)
        if dists[D][cnt] != float('inf')
    ]

    answer = apply_tax(0, candidates)
    print(answer)

    total_tax = 0
    for _ in range(K):
        p = int(input())
        total_tax += p

        answer = apply_tax(total_tax, candidates)
        print(answer)


if __name__ == '__main__':
    main()
