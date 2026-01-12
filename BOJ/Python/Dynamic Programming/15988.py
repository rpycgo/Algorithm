import sys


def main():
    input = sys.stdin.readline

    T = int(input())

    MAX_N = 1_000_000

    dp = [0] * (MAX_N+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, MAX_N+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009

    for _ in range(T):
        n = int(input())

        print(dp[n])


if __name__ == '__main__':
    main()
