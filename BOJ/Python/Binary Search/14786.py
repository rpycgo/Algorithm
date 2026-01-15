import sys
from math import sin


input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    left = 0
    right = 200_000

    for _ in range(100):
        mid = (left+right) / 2

        if A*mid + B*sin(mid) > C:
            right = mid
        else:
            left = mid

    print(left)


if __name__ == '__main__':
    main()
