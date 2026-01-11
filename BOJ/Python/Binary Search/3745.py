import sys
from bisect import bisect_left


def main():
    input = sys.stdin.read

    data = input().split()

    ptr = 0
    total_len = len(data)

    while ptr < total_len:
        N = int(data[ptr])
        ptr += 1

        prices = data[ptr:ptr+N]
        ptr += N

        LIS = []
        for price in prices:
            price = int(price)

            idx = bisect_left(LIS, price)

            if idx == len(LIS):
                LIS.append(price)
            else:
                LIS[idx] = price

        print(len(LIS))


if __name__ == '__main__':
    main()
    