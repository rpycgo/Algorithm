import sys


input = sys.stdin.readline


def main():
    N = int(input())

    dp = [1] * (N+1)
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    answer = 2 * (dp[-1]+dp[-2])
    print(answer)


if __name__ == '__main__':
    main()
