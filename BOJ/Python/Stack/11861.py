import sys


input = sys.stdin.readline


def main():
    N = int(input())
    D = list(map(int, input().split())) + [0]

    stack = []
    max_area = float('-inf')

    for i, curr_h in enumerate(D):
        while stack and curr_h <= D[stack[-1]]:
            target_idx = stack.pop()
            height = D[target_idx]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            max_area = max(max_area, height*width)

        stack.append(i)

    print(max_area)


if __name__ == '__main__':
    main()
