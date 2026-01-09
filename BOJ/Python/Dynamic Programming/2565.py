import sys


def main():
    input = sys.stdin.readline

    n = int(input())

    cables = []
    for _ in range(n):
        cable = list(map(int, input().split()))
        cables.append(cable)

    cables.sort(key=lambda x: (x[0], x[1]))
    B = [cable[1] for cable in cables]

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if B[j] < B[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(n - max(dp))


if __name__ == '__main__':
    main()
