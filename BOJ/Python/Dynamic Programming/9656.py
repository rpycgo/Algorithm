import sys


input = sys.stdin.readline


def main():
    N = int(input())

    if N == 1 or N == 3:
        print('CY')
        return
    if N == 2:
        print('SK')
        return

    dp = [0] * (N+1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 0

    for i in range(4, N+1):
        if dp[i-1] == 0 or dp[i-3] == 0:
            dp[i] = 1
        else:
            dp[i] = 0

    answer = 'SK' if dp[N] == 1 else 'CY'
    print(answer)


if __name__ == '__main__':
    main()
