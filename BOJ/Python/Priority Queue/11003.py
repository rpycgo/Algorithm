import sys
from collections import deque


input = sys.stdin.readline


def main():
    N, L = map(int, input().split())
    D = list(map(int, input().split()))

    dq = deque()
    for i in range(N):
        while dq and dq[-1][0] >= D[i]:
            dq.pop()

        dq.append((D[i], i))

        if dq[0][1] <= i - L:
            dq.popleft()

        print(dq[0][0], end=' ')


if __name__ == '__main__':
    main()
