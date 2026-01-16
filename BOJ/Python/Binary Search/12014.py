import sys
from bisect import bisect_left


input = sys.stdin.readline


def main():
    T = int(input())
    for i in range(1, T+1):
        N, K = map(int, input().split())
        prices = list(map(int, input().split()))

        LIS = []

        for price in prices:
            if not LIS or LIS[-1] < price:
                LIS.append(price)
            else:
                idx = bisect_left(LIS, price)
                LIS[idx] = price

        answer = 1 if len(LIS) >= K else 0
        print(f'Case #{i}')
        print(answer)


if __name__ == '__main__':
    main()
