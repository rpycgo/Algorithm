import sys
from math import ceil


def calculate_minimum_jealousy(jealousy, jewels):
    count = 0
    for jewel in jewels:
        count += ceil(jewel/jealousy)

    return count


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    jewels = [int(input()) for _ in range(M)]

    left = 1
    right = max(jewels)

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_minimum_jealousy(mid, jewels) <= N:
            answer = mid
            right = mid -1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
