import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    n = int(input())

    cables = []
    for _ in range(n):
        cable = list(map(int, input().split()))
        cables.append(cable)

    cables.sort(key=lambda x: (x[0], x[1]))
    B = [cable[1] for cable in cables]

    LIS = []
    for cable in B:
        idx = bisect_left(LIS, cable)

        if not LIS or len(LIS) == idx:
            LIS.append(cable)
        else:
            LIS[idx] = cable

    answer = n - len(LIS)

    print(answer)


if __name__ == '__main__':
    main()
