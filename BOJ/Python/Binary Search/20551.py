import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    D = [int(input()) for _ in range(M)]

    A.sort()

    for num in D:
        idx = bisect_left(A, num)

        if idx < N and A[idx] == num:
            print(idx)
        else:
            print(-1)


if __name__ == '__main__':
    main()
