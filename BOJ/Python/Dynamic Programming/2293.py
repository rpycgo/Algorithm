import sys


def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k+1):
            dp[i] += dp[i-coin]

    answer = dp[-1]

    print(answer)


if __name__ == '__main__':
    main()
