import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        N = int(input())
        notes1 = list(map(int, input().split()))
        M = int(input())
        notes2 = list(map(int, input().split()))

        notes1.sort()
        for num in notes2:
            idx = bisect_left(notes1, num)

            if idx < N and notes1[idx] == num:
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()
