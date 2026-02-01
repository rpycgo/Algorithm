import sys


input = sys.stdin.readline


def main():
    N = int(input())
    heights = [int(input()) for _ in range(N)] + [0]

    max_cut_area = float('-inf')
    stack = []
    for i, curr_h in enumerate(heights):
        while stack and curr_h <= heights[stack[-1]]:
            target_idx = stack.pop()
            height = heights[target_idx]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            max_cut_area = max(max_cut_area, height*width)

        stack.append(i)

    print(max_cut_area)


if __name__ == '__main__':
    main()
