import sys


input = sys.stdin.readline


def main():
    MAX = 10001
    dp = [1] * MAX

    for i in range(2, MAX):
        dp[i] += dp[i-2]

    for i in range(3, MAX):
        dp[i] += dp[i-3]

    T = int(input())
    for _ in range(T):
        n = int(input())
        answer = dp[n]

        print(answer)


if __name__ == '__main__':
    main()
