import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    N, T = map(int, input().split())

    min_bus_time = float('inf')
    for _ in range(N):
        S, I, C = map(int, input().split())

        curr_min_bus_time = float('inf')

        left = 0
        right = C - 1

        answer = right
        while left <= right:
            mid = (left+right) // 2

            bus_time = S + (I*mid)

            if bus_time >= T:
                curr_min_bus_time = bus_time
                right = mid - 1
            else:
                left = mid + 1

        if curr_min_bus_time < min_bus_time:
            min_bus_time = curr_min_bus_time

    answer = -1 if min_bus_time == float('inf') else min_bus_time - T

    print(answer)


if __name__ == '__main__':
    main()
