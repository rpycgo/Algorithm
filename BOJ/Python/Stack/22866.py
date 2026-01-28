import sys


input = sys.stdin.readline


def main():
    N = int(input())
    heights = [0] + list(map(int, input().split()))

    counts = [0] * (N+1)
    nearest_dist = [float('inf')] * (N+1)
    nearest_idx = [0] * (N+1)


    stack = []
    for i in range(1, N+1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()

        counts[i] += len(stack)

        if stack:
            dist = i - stack[-1]

            if dist < nearest_dist[i]:
                nearest_dist[i] = dist
                nearest_idx[i] = stack[-1]

        stack.append(i)

    stack = []
    for i in range(N, 0, -1):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()

        counts[i] += len(stack)

        if stack:
            dist = stack[-1] - i

            if dist < nearest_dist[i]:
                nearest_dist[i] = dist
                nearest_idx[i] = stack[-1]
            elif dist == nearest_dist[i]:
                nearest_idx[i] = min(nearest_idx[i], stack[-1])

        stack.append(i)

    for i in range(1, N+1):
        if counts[i] == 0:
            print(0)
        else:
            print(f'{counts[i]} {nearest_idx[i]}')


if __name__ == '__main__':
    main()
