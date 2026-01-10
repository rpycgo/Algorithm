import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    heights = [int(input()) for _ in range(N)]
    heights.append(0)

    max_area = 0
    stack = [0]

    for i in range(1, N+1):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]

            if not stack:
                w = i
            else:
                w = i - stack[-1] - 1

            max_area = max(max_area, h * w)

        stack.append(i)

    print(max_area)


if __name__ == '__main__':
    main()
