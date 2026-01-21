import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()

    if string[0] == '0':
        print(0)
        return

    n = len(string)
    dp = [0] * (n+1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        if int(string[i-1]) > 0:
            dp[i] += dp[i-1]

        two_digits = int(string[i-2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]

        dp[i] %= 1_000_000

    answer = dp[n]
    print(answer)


if __name__ == '__main__':
    main()
