import sys


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())

    packages = []
    for _ in range(N):
        package = list(map(int, input().split()))
        packages.append(package)

    dp = [0] * (K+1)
    for package in packages:
        W, V = package

        for j in range(K, W-1, -1):
            dp[j] = max(dp[j], dp[j-W] + V)

    print(dp[K])


if __name__ == '__main__':
    main()
