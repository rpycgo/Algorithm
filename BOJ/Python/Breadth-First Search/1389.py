import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())

    graph = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())

        graph[u].append(v)
        graph[v].append(u)

    min_bacon = float('inf')
    answer = 0

    for i in range(1, N+1):
        visited = [-1] * (N+1)
        visited[i] = 0
        queue = deque([i])

        while queue:
            curr_node = queue.popleft()

            for neighbor in graph[curr_node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[curr_node] + 1
                    queue.append(neighbor)

        curr_bacon = sum(v for v in visited if v > 0)
        if curr_bacon < min_bacon:
            min_bacon = curr_bacon
            answer = i

    print(answer)


if __name__ == '__main__':
    main()
