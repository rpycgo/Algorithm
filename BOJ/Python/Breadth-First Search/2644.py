import sys
from collections import deque


def main():
    input = sys.stdin.readline

    n = int(input())
    start, end = map(int, input().split())
    m = int(input())

    relations = [[] * 2 for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())

        relations[x].append(y)
        relations[y].append(x)

    distances = [-1] * (n + 1)
    distances[start] = 0

    queue = deque([start])
    while queue:
        curr = queue.popleft()

        if curr == end:
            print(distances[curr])
            return

        for adj in relations[curr]:
            if distances[adj] == -1:
                distances[adj] = distances[curr] + 1
                queue.append(adj)

    print(-1)


if __name__ == '__main__':
    main()
