import sys


def main():
    input = sys.stdin.readline

    n = int(input())

    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(2, n+1):
        if i >= 2:
            dp[i] = min(dp[i], dp[i-2]+1)

        if i >= 5:
            dp[i] = min(dp[i], dp[i-5]+1)

    answer = -1 if dp[n] == float('inf') else dp[n]

    print(answer)


if __name__ == '__main__':
    main()
