import sys
from collections import deque


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    move_map = {}
    for _ in range(N+M):
        u, v = map(int, input().split())
        move_map[u] = v

    visited = [False] * 101
    visited[1] = True

    queue = deque([(1, 0)])
    while queue:
        curr, cnt = queue.popleft()

        if curr == 100:
            print(cnt)
            return

        for i in range(1, 7):
            next = curr + i

            if next <= 100:
                if next in move_map:
                    next = move_map[next]

                if not visited[next]:
                    visited[next] = True
                    queue.append((next, cnt+1))


if __name__ == '__main__':
    main()
