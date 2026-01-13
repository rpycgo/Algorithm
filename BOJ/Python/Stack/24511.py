import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    M = int(input())
    C = list(map(int, input().split()))

    queue = deque()
    for i in range(N):
        if A[i] == 0:
            queue.append(B[i])

    results = []
    for x in C:
        queue.appendleft(x)

        results.append(queue.pop())

    print(*(results))


if __name__ == '__main__':
    main()
