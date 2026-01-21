import sys


input = sys.stdin.readline


def main():
    n = int(input())

    if n == 0 or n == 1:
        print(n)
        return

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    answer = dp[n-1]
    print(answer)


if __name__ == '__main__':
    main()
