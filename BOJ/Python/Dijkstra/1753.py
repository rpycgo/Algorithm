import sys
import heapq


def dijkstra(start, distances, graph):
    queue = []
    heapq.heappush(queue, (0, start))

    distances[start] = 0

    while queue:
        distance, curr_node = heapq.heappop(queue)

        if distances[curr_node] < distance:
            continue

        for next_node, weight in graph[curr_node]:
            cost = distance + weight

            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


def main():
    input = sys.stdin.readline

    V, E = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    distances = [float('inf')] * (V+1)

    dijkstra(start, distances, graph)

    for i in range(1, V+1):
        if distances[i] == float('inf'):
            print('INF')
        else:
            print(distances[i])


if __name__ == '__main__':
    main()
