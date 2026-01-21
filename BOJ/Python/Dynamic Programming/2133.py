import sys


input = sys.stdin.readline


def main():
    N = int(input())

    if N%2 != 0:
        print(0)
        return

    dp = [0] * (N+1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3

        for j in range(i-4, -1, -2):
            dp[i] += dp[j]*2

    answer = dp[N]
    print(answer)


if __name__ == '__main__':
    main()
