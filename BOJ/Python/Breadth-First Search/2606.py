import sys
from collections import deque


def main():
    input = sys.stdin.readline

    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)
    visited[1] = True
    queue = deque([1])
    answer = 0

    while queue:
        current_node = queue.popleft()

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                answer += 1

    print(answer)


if __name__ == '__main__':
    main()
