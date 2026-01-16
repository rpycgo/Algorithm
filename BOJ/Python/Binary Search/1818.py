import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    N = int(input())
    book_order = list(map(int, input().split()))

    LIS = []
    for rank in book_order:
        if not LIS or rank > LIS[-1]:
            LIS.append(rank)
        else:
            idx = bisect_left(LIS, rank)
            LIS[idx] = rank

    answer = N - len(LIS)
    print(answer)


if __name__ == '__main__':
    main()
