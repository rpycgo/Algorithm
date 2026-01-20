import sys
from collections import deque


input = sys.stdin.readline


def is_connecteed(nodes, adj):
    if not nodes:
        return False

    visited = {nodes[0]}
    queue = deque([nodes[0]])

    while queue:
        curr_node = queue.popleft()

        for neighbor in adj[curr_node]:
            if neighbor in nodes and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == len(nodes)


def main():
    N = int(input())
    populations = tuple(map(int, input().split()))

    adj = [[] for _ in range(N)]

    for i in range(N):
        _, *neighbors = map(int, input().split())
        for n in neighbors:
            adj[i].append(n-1)

    min_diff = float('inf')
    for i in range(1, (1 << N)-1):
        group_a = []
        group_b = []

        for j in range(N):
            if i & (1 << j):
                group_a.append(j)
            else:
                group_b.append(j)

        if is_connecteed(group_a, adj) and is_connecteed(group_b, adj):
            population_a = sum(populations[idx] for idx in group_a)
            population_b = sum(populations[idx] for idx in group_b)

            diff = abs(population_a - population_b)
            if diff < min_diff:
                min_diff = diff

    answer = min_diff if min_diff != float('inf') else -1
    print(answer)


if __name__ == '__main__':
    main()
