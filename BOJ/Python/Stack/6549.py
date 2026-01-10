import sys


def main():
    input = sys.stdin.readline

    while True:
        n, *heights = list(map(int, input().split()))

        if n == 0:
            break

        heights.append(0)

        stack = [0]
        max_area = 0

        for i in range(1, n+1):
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
