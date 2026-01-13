import sys
from collections import deque


def main():
    input = sys.stdin.readline

    N, M, K, X = map(int, input().split())

    answer = [-1] * (N+1)
    answer[X] = 0

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())

        graph[u].append(v)

    queue = deque([X])
    while queue:
        curr_node = queue.popleft()

        for neighbor in graph[curr_node]:
            if answer[neighbor] == -1:
                answer[neighbor] = answer[curr_node] + 1
                queue.append(neighbor)

    is_found = False
    for i in range(1, N+1):
        if answer[i] == K:
            is_found = True

            print(i)

    if not is_found:
        print(-1)



if __name__ == '__main__':
    main()
        