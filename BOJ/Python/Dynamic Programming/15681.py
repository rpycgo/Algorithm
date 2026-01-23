import sys


sys.setrecursionlimit(2*10**6)
input = sys.stdin.readline


def get_n_subtree_node(curr_node, prev_node, subtree_size, adj):
    subtree_size[curr_node] = 1

    for neighbor_node in adj[curr_node]:
        if neighbor_node != prev_node:
            get_n_subtree_node(neighbor_node, curr_node, subtree_size, adj)
            subtree_size[curr_node] += subtree_size[neighbor_node]


def main():
    N, R, Q = map(int, input().split())

    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    subtree_size = [0] * (N+1)
    get_n_subtree_node(R, -1, subtree_size, adj)

    for _ in range(Q):
        u = int(input())
        print(subtree_size[u])


if __name__ == '__main__':
    main()
