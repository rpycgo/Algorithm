import sys
from collections import deque


def main():
    input = sys.stdin.readline

    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        colors = [0] * (V+1)

        for _ in range(E):
            u, v = map(int, input().split())

            graph[u].append(v)
            graph[v].append(u)

        is_bipartite = True
        for i in range(1, V+1):
            if colors[i] == 0:
                queue = deque([i])
                colors[i] = 1

                while queue:
                    curr_idx = queue.popleft()

                    for neighbor in graph[curr_idx]:
                        if colors[neighbor] == 0:
                            colors[neighbor] = 3 - colors[curr_idx]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[curr_idx]:
                            is_bipartite = False
                            break

                    if not is_bipartite:
                        break

            if not is_bipartite:
                break

        answer = 'YES' if is_bipartite else 'NO'

        print(answer)


if __name__ == '__main__':
    main()
