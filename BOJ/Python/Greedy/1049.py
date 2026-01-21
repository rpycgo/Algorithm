import sys


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())

    min_package = float('inf')
    min_single = float('inf')

    for _ in range(M):
        P, S = map(int, input().split())

        if P < min_package:
            min_package = P
        if S < min_single:
            min_single = S

    if min_single*6 < min_package:
        min_package = min_single*6

    case1 = (N//6)*min_package + (N%6)*min_single
    case2 = ((N//6) + 1) * min_package
    case3 = N * min_single

    answer = min(case1, case2, case3)
    print(answer)


if __name__ == '__main__':
    main()
