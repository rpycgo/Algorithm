import sys


input = sys.stdin.readline


def main():
    n = int(input())
    box_sizes = list(map(int, input().split()))

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if box_sizes[j] < box_sizes[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    answer = max(dp)
    print(answer)


if __name__ == '__main__':
    main()
