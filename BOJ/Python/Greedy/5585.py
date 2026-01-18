import sys


input = sys.stdin.readline


def main():
    coins = (500, 100, 50, 10, 5, 1)

    prices = int(input())
    changes = 1000 - prices

    cnt = 0
    for coin in coins:
        n_coins = changes // coin

        cnt += n_coins
        changes %= coin

    print(cnt)


if __name__ == '__main__':
    main()
