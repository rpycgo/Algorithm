import sys


def main():
    def tsp(curr, visited):
        if visited == (1 << N) - 1:
            return W[curr][0] if W[curr][0] > 0 else float('inf')

        if dp[curr][visited] != -1:
            return dp[curr][visited]

        dp[curr][visited] = float('inf')

        for next_node in range(N):
            if W[curr][next_node] > 0 and not (visited & (1 << next_node)):
                res = tsp(next_node, visited | (1 << next_node))
                dp[curr][visited] = min(dp[curr][visited], res + W[curr][next_node])

        return dp[curr][visited]

    input = sys.stdin.readline

    N = int(input())
    W = [
        list(map(int, input().split()))
        for _
        in range(N)
    ]

    dp = [[-1]*(1 << N) for _ in range(N)]

    answer = tsp(0, 1 << 0)

    print(answer)


if __name__ == '__main__':
    main()
