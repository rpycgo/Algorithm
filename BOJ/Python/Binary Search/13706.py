import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    left = 1
    right = N

    while left <= right:
        mid = (left+right) // 2

        if mid*mid == N:
            print(mid)
            return

        if mid*mid < N:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    main()
