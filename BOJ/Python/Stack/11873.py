import sys


input = sys.stdin.readline


def calculate_max_area(heights):
    heights = heights[:] + [0]
    stack = []
    max_area = 0

    for i, curr_h in enumerate(heights):
        while stack and curr_h < heights[stack[-1]]:
            target_idx = stack.pop()
            height = heights[target_idx]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            max_area = max(max_area, height*width)

        stack.append(i)

    return max_area


def main():
    while True:
        N, M = map(int, input().split())

        if N == 0 and M == 0:
            return

        heights = [0] * M
        max_area = float('-inf')

        for _ in range(N):
            row = map(int, input().split())

            for j, val in enumerate(row):
                if val == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            curr_area = calculate_max_area(heights)
            max_area = max(max_area, curr_area)

        print(max_area)


if __name__ == '__main__':
    main()
