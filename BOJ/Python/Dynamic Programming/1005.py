import sys
from collections import deque


input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())

        indegrees = [0] * (N+1)
        results = [0] * (N+1)

        times = [0] * (N+1)
        D = map(int, input().split())
        for i, d in enumerate(D, start=1):
            times[i] = d

        adj = [[] for _ in range(N+1)]
        for _ in range(K):
            pre, post = map(int, input().split())

            adj[pre].append(post)
            indegrees[post] += 1

        queue = deque()
        for i in range(1, N+1):
            if indegrees[i] == 0:
                queue.append(i)
                results[i] = times[i]

        while queue:
            curr_node = queue.popleft()

            for next_node in adj[curr_node]:
                indegrees[next_node] -= 1

                results[next_node] = max(results[next_node], results[curr_node] + times[next_node])

                if indegrees[next_node] == 0:
                    queue.append(next_node)

        W = int(input())
        answer = results[W]
        print(answer)


if __name__ == '__main__':
    main()
