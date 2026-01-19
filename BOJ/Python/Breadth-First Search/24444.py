import sys
from collections import deque


input = sys.stdin.readline


def bfs(N, M, start_node, adj):
    cnt = 1

    order = [0] * (N+1)
    order[start_node] = cnt

    queue = deque([start_node])
    while queue:
        curr_node = queue.popleft()

        for next_node in adj[curr_node]:
            if order[next_node] == 0:
                cnt += 1
                order[next_node] = cnt
                queue.append(next_node)

    return order


def main():
    N, M, R = map(int, input().split())

    adj = [[] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, N+1):
        adj[i].sort()

    order = bfs(N, M, R, adj)
    for i in range(1, N+1):
        print(order[i])


if __name__ == '__main__':
    main()
