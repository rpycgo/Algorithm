import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    N = int(input())
    F = list(map(int, input().split()))

    F.sort()

    total_pairs = 0
    for i in range(1, N):
        target = F[i] * 0.9

        idx = bisect_left(F, target, 0, i)

        total_pairs += (i - idx)

    print(total_pairs)


if __name__ == '__main__':
    main()
