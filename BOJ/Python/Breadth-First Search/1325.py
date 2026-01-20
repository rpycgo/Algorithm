import sys
from collections import deque


input = sys.stdin.readline


def bfs(start_node, N, adj):
    visited = [False] * (N + 1)
    visited[start_node] = True

    cnt = 1

    queue = deque([start_node])
    while queue:
        curr_node = queue.popleft()

        for neighbor in adj[curr_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

                cnt += 1

    return cnt


def main():
    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())

        adj[v].append(u)

    max_idx = []
    n_max_hack = 0
    for i in range(1, N+1):
        if not adj[i]:
            curr_max = 1
        else:
            curr_max = bfs(i, N, adj)

        if curr_max > n_max_hack:
            n_max_hack = curr_max

            max_idx.clear()
            max_idx.append(i)
        elif curr_max == n_max_hack:
            max_idx.append(i)

    print(*max_idx)


if __name__ == '__main__':
    main()
