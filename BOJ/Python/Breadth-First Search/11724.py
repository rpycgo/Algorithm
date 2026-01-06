import sys
from collections import deque


def bfs(start_node, visited, graph):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N+1)

    answer = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i, visited, graph)
            answer += 1

    print(answer)


if __name__ == '__main__':
    main()
