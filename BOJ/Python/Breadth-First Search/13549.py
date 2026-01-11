import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())

    MAX = 100_001
    time = [-1] * MAX
    time[N] = 0

    dx = (-1, 1)

    queue = deque([N])
    while queue:
        curr = queue.popleft()

        if curr == K:
            print(time[curr])

        nx = curr * 2
        if 0 <= nx < MAX and time[nx] == -1:
            time[nx] = time[curr]
            queue.appendleft(nx)

        for i in range(2):
            nx = curr + dx[i]
            if 0 <= nx < MAX and time[nx] == -1:
                time[nx] = time[curr] + 1
                queue.append(nx)


if __name__ == '__main__':
    main()
