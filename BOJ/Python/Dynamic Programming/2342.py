import sys


input = sys.stdin.readline


def get_cost(start, end):
    if start == 0:
        return 2
    if start == end:
        return 1
    if abs(start-end) == 2:
        return 4
    return 3


def main():
    seqs = list(map(int, input().split()))

    if seqs[0] == 0:
        print(0)
        return

    n = len(seqs) - 1
    dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(n+1)]

    dp[0][0][0] = 0

    for i in range(n):
        target = seqs[i]

        for left in range(5):
            for right in range(5):
                if dp[i][left][right] != float('inf'):
                    curr_cost = dp[i][left][right]

                    if target != right:
                        new_cost = curr_cost + get_cost(left, target)

                        if new_cost < dp[i+1][target][right]:
                            dp[i+1][target][right] = new_cost

                    if target != left:
                        new_cost = curr_cost + get_cost(right, target)

                        if new_cost < dp[i+1][left][target]:
                            dp[i+1][left][target] = new_cost

    answer = float('inf')
    for right in range(5):
        for left in range(5):
            answer = min(answer, dp[n][left][right])

    print(answer)


if __name__ == '__main__':
    main()
