import sys
from collections import deque


input = sys.stdin.readline


def bfs(start_node, N, graph):
    visited = [False] * (N+1)
    visited[start_node] = True

    cnt = 1
    order = [0] * (N+1)
    order[start_node] = cnt

    queue = deque([start_node])
    while queue:
        curr_node = queue.popleft()

        graph[curr_node].sort(reverse=True)

        for neighbor_node in graph[curr_node]:
            if not visited[neighbor_node]:
                visited[neighbor_node] = True
                queue.append(neighbor_node)

                cnt += 1
                order[neighbor_node] = cnt

    return order


def main():
    N, M, R = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    order = bfs(R, N, adj)

    for i in range(1, N+1):
        print(order[i])


if __name__ == '__main__':
    main()
