import sys


input = sys.stdin.readline


def main():
    D, K = map(int, input().split())

    dp = [0] * (D-1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, D-1):
        dp[i] = dp[i-1] + dp[i-2]

    for a in range(1, K//dp[-2]):
        remaining = K - (dp[-2] * a)

        if remaining%dp[-1] == 0:
            b = remaining // dp[-1]

            if a <= b:
                print(a)
                print(b)

                return


if __name__ == '__main__':
    main()
