import sys


input = sys.stdin.readline


def main():
    coins = (25, 10, 5, 1)

    T = int(input())
    for _ in range(T):
        C = int(input())

        cnts = [0] * 4
        for i, coin in enumerate(coins):
            n_coins = C // coin

            cnts[i] = n_coins
            C %= coin

        cnts = map(str, cnts)
        answer = ' '.join(cnts)
        print(answer)


if __name__ == '__main__':
    main()
