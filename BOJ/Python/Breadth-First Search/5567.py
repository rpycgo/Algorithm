import sys
from collections import deque


input = sys.stdin.readline


def main():
    n = int(input())
    m = int(input())

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n+1)

    queue = deque([(1, 0)])
    visited[1] = True

    n_invitations = 0
    while queue:
        curr_node, dist = queue.popleft()

        if dist >= 2:
            continue

        for next_node in adj[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist+1))
                n_invitations += 1

    print(n_invitations)


if __name__ == '__main__':
    main()
