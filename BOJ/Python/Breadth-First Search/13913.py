import sys
from collections import deque


input = sys.stdin.readline


def main():
    MAX = 100_000
    N, K = map(int, input().split())

    dist = [-1] * (MAX+1)
    parent = [-1] * (MAX+1)

    dist[N] = 0
    queue = deque([N])

    while queue:
        curr_node = queue.popleft()

        if curr_node == K:
            path = []

            temp = curr_node
            while temp != -1:
                path.append(temp)
                temp = parent[temp]

            print(dist[curr_node])
            print(*path[::-1])

            return

        for next_node in (curr_node-1, curr_node+1, curr_node*2):
            if 0 <= next_node <= MAX and dist[next_node] == -1:
                dist[next_node] = dist[curr_node] + 1
                parent[next_node] = curr_node

                queue.append(next_node)


if __name__ == '__main__':
    main()
