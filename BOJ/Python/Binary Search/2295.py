import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    U = [int(input()) for _ in range(N)]
    U.sort()

    sum_xy = set()
    for x in U:
        for y in U:
            sum_xy.add(x + y)
    sum_xy = list(sum_xy)
    sum_xy.sort()

    U.sort(reverse=True)

    for k in U:
        for z in U:
            target = k - z

            idx = bisect_left(sum_xy, target)
            if idx < len(sum_xy) and sum_xy[idx] == target:
                print(k)
                return


if __name__ == '__main__':
    main()
