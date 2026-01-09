import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input())
    utility_poles = list(map(int, input().split()))

    LIS = []
    for utility_pole in utility_poles:
        idx = bisect_left(LIS, utility_pole)

        if not utility_pole or len(LIS) == idx:
            LIS.append(utility_pole)
        else:
            LIS[idx] = utility_pole

    answer = N - len(LIS)

    print(answer)


if __name__ == '__main__':
    main()
