import sys


input = sys.stdin.readline


def main():
    N = int(input())
    weights = tuple(map(int, input().split()))
    M = int(input())
    marble_weights = tuple(map(int, input().split()))

    total_weights = sum(weights)

    dp = [[False] * (total_weights + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i, weight in enumerate(weights, start=1):
        for j in range(total_weights+1):
            if dp[i-1][j]:
                dp[i][j] = True

                if j + weight <= total_weights:
                    dp[i][j+weight] = True

                dp[i][abs(j - weight)] = True

    for marble_weight in marble_weights:
        if marble_weight > total_weights:
            print('N', end=' ')
        elif dp[N][marble_weight]:
            print('Y', end=' ')
        else:
            print('N', end=' ')


if __name__ == '__main__':
    main()
