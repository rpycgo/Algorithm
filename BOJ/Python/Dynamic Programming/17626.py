import sys


def main():
    input = sys.stdin.readline

    n = int(input())

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        min_val = 4

        j = 1
        while j*j <= i:
            min_val = min(min_val, dp[i - j*j])
            j += 1

        dp[i] = min_val + 1

    answer = dp[n]

    print(answer)


if __name__ == '__main__':
    main()
