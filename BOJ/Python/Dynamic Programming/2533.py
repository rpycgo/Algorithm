import sys


sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(curr_node, visited, dp, adj):
    visited[curr_node] = True

    for neighbor_node in adj[curr_node]:
        if not visited[neighbor_node]:
            dfs(neighbor_node, visited, dp, adj)

            dp[curr_node][0] += dp[neighbor_node][1]
            dp[curr_node][1] += min(dp[neighbor_node][0], dp[neighbor_node][1])


def main():
    N = int(input())

    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 1] for _ in range(N+1)]
    visited = [False] * (N+1)

    dfs(1, visited, dp, adj)

    answer = min(dp[1][0], dp[1][1])
    print(answer)


if __name__ == '__main__':
    main()
