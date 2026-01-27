import sys


input = sys.stdin.readline


def main():
    N = int(input())
    L = tuple(map(int, input().split()))
    J = tuple(map(int, input().split()))

    dp = [0] * 100
    for i in range(N):
        loss = L[i]
        joy = J[i]

        for hp in range(99, loss-1, -1):
            if dp[hp-loss] + joy > dp[hp]:
                dp[hp] = dp[hp-loss] + joy

    answer = max(dp)
    print(answer)


if __name__ == '__main__':
    main()
