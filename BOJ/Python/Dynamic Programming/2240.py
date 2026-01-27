import sys


input = sys.stdin.readline


def main():
    T, W = map(int, input().split())
    plums = [0] + [int(input()) for _ in range(T)]

    dp = [[0] * (W+1) for _ in range(T+1)]
    for t in range(1, T+1):
        curr_plum = plums[t]

        for w in range(W+1):
            pos = 1 if w%2 == 0 else 2

            can_get = 1 if pos == curr_plum else 0

            dp[t][w] = dp[t-1][w] + can_get

            if w > 0:
                dp[t][w] = max(dp[t][w], dp[t-1][w-1]+can_get)

    answer = max(dp[T])
    print(answer)


if __name__ == '__main__':
    main()
