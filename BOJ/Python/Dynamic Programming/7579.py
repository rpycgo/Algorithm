import sys


input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    max_cost = sum(costs)
    dp = [0] * (max_cost + 1)

    for i in range(N):
        curr_memory = memories[i]
        curr_cost = costs[i]

        for j in range(max_cost, curr_cost-1, -1):
            dp[j] = max(dp[j], dp[j-curr_cost] + curr_memory)

    for cost in range(max_cost+1):
        if dp[cost] >= M:
            answer = cost
            break

    print(answer)


if __name__ == '__main__':
    main()
