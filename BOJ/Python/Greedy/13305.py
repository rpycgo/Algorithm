import sys


input = sys.stdin.readline


def main():
    N = int(input())
    distances = list(map(int, input().split()))
    oil_prices = list(map(int, input().split()))

    min_price = oil_prices[0]
    total_cost = 0

    for i in range(N-1):
        if oil_prices[i] < min_price:
            min_price = oil_prices[i]

        total_cost += min_price * distances[i]

    print(total_cost)


if __name__ == '__main__':
    main()
