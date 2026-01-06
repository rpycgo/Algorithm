import sys
from collections import deque


def bfs(mid, n, start_node, end_node, graph):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        if current_node == end_node:
            return True

        for neighbor, weight in graph[current_node]:
            if not visited[neighbor] and weight >= mid:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    max_weight = 0
    for _ in range(M):
        u, v, w = map(int, input().split())

        graph[u].append((v, w))
        graph[v].append((u, w))

        max_weight = max(max_weight, w)

    start_node, end_node = map(int, input().split())

    left = 1
    right = max_weight
    answer = 0

    while left <= right:
        mid = (left+right) // 2

        if bfs(mid, N, start_node, end_node, graph):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
