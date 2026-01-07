import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    dp = [i for i in range(N+1)]

    for i in range(1, N+1):
        j = 1
        while j*j <= i:
            if dp[i] > dp[i - j*j] + 1:
                dp[i] = dp[i - j*j] + 1

            j+=1

    print(dp[N])


if __name__ == '__main__':
    main()
