import sys
from collections import deque


input = sys.stdin.readline


def main():
    N, D = map(int, input().split())
    K = list(map(int, input().split()))

    dp = [0] * N
    queue = deque()

    for i in range(N):
        if queue and queue[0][1] < i - D:
            queue.popleft()

        prev_max = queue[0][0] if queue else 0
        dp[i] = max(0, prev_max) + K[i]

        while queue and queue[-1][0] <= dp[i]:
            queue.pop()

        queue.append((dp[i], i))

    answer = max(dp)
    print(answer)


if __name__ == '__main__':
    main()
