import sys


input = sys.stdin.readline


def main():
    N = int(input())

    dp = [0] * 1001
    dp[1:5] = [1, 0, 1, 1]

    for i in range(5, N+1):
        if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
            dp[i] = 1
        else:
            dp[i] = 0

    answer = 'SK' if dp[N] == 1 else 'CY'
    print(answer)


if __name__ == '__main__':
    main()
