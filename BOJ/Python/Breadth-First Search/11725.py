import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N = int(input())

    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())

        tree[u].append(v)
        tree[v].append(u)

    parent = [0] * (N + 1)
    parent[1] = 1

    queue = deque([1])
    while queue:
        curr = queue.popleft()

        for nx in tree[curr]:
            if parent[nx] == 0:
                parent[nx] = curr
                queue.append(nx)

    answer = '\n'.join(map(str, parent[2:]))

    print(answer)


if __name__ == '__main__':
    main()
