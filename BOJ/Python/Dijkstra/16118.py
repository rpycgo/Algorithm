import sys
import heapq


input = sys.stdin.readline


def dijkstra(start_node, N, adj):
    dists_fox = [float('inf')] * (N+1)
    dists_fox[start_node] = 0

    heap_fox = [(0, start_node)]
    while heap_fox:
        curr_cost, curr_node = heapq.heappop(heap_fox)

        if dists_fox[curr_node] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            new_cost = curr_cost + next_weight

            if new_cost < dists_fox[next_node]:
                dists_fox[next_node] = new_cost
                heapq.heappush(heap_fox, (new_cost, next_node))

    dists_wolf = [[float('inf')] * 2 for _ in range(N+1)]
    dists_wolf[start_node][0] = 0

    heap_wolf = [(0, start_node, 0)]
    while heap_wolf:
        curr_cost, curr_node, curr_state = heapq.heappop(heap_wolf)

        if dists_wolf[curr_node][curr_state] < curr_cost:
            continue

        for next_node, next_weight in adj[curr_node]:
            if curr_state == 0:
                next_cost = curr_cost + next_weight//2

                if next_cost < dists_wolf[next_node][1]:
                    dists_wolf[next_node][1] = next_cost
                    heapq.heappush(heap_wolf, (next_cost, next_node, 1))
            else:
                next_cost = curr_cost + next_weight*2

                if next_cost < dists_wolf[next_node][0]:
                    dists_wolf[next_node][0] = next_cost
                    heapq.heappush(heap_wolf, (next_cost, next_node, 0))

    cnt = 0
    for i in range(2, N+1):
        if dists_fox[i] < min(dists_wolf[i]):
            cnt += 1

    return cnt


def main():
    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, d = map(int, input().split())

        adj[a].append((b, d*2))
        adj[b].append((a, d*2))

    answer = dijkstra(1, N, adj)
    print(answer)


if __name__ == '__main__':
    main()
