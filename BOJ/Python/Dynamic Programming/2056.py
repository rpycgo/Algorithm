import sys
from collections import deque


input = sys.stdin.readline


def main():
    N = int(input())

    indegrees = [0] * (N+1)
    times = [0] * (N+1)
    results = [0] * (N+1)

    adj = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        data = tuple(map(int, input().split()))
        times[i] = data[0]

        for pre in data[2:]:
            adj[pre].append(i)
            indegrees[i] += 1

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

    answer = max(results)
    print(answer)


if __name__ == '__main__':
    main()
