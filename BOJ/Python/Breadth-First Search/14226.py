import sys
from collections import deque


input = sys.stdin.readline


def main():
    S = int(input())

    dists = [[-1] * 1001 for _ in range(1001)]

    queue = deque([(1, 0)])
    dists[1][0] = 0

    while queue:
        n_displays, n_clipboards = queue.popleft()

        if n_displays == S:
            print(dists[n_displays][n_clipboards])
            return

        if dists[n_displays][n_displays] == -1:
            dists[n_displays][n_displays] = dists[n_displays][n_clipboards] + 1
            queue.append((n_displays, n_displays))

        if n_clipboards > 0 and n_displays+n_clipboards <= 1000:
            dists[n_displays+n_clipboards][n_clipboards] = dists[n_displays][n_clipboards] + 1
            queue.append((n_displays+n_clipboards, n_clipboards))

        if n_displays-1 >= 0 and dists[n_displays-1][n_clipboards] == -1:
            dists[n_displays-1][n_clipboards] = dists[n_displays][n_clipboards] + 1
            queue.append((n_displays-1, n_clipboards))


if __name__ == '__main__':
    main()
