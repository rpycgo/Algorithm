import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    coords = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    coords.sort()

    left_stack = []
    for coord in coords:
        if not left_stack or coord[1] > left_stack[-1][1]:
            left_stack.append(coord)

    right_stack = []
    for coord in reversed(coords):
        if not right_stack or coord[1] > right_stack[-1][1]:
            right_stack.append(coord)

    area = 0
    for i in range(len(left_stack)-1):
        width = left_stack[i+1][0] - left_stack[i][0]
        height = left_stack[i][1]

        area += width * height

    for i in range(len(right_stack)-1):
        width = right_stack[i][0] - right_stack[i+1][0]
        height = right_stack[i][1]

        area += abs(width) * height

    max_h = left_stack[-1][1]
    width = abs(right_stack[-1][0] - left_stack[-1][0]) + 1
    area += width * max_h

    print(area)


if __name__ == '__main__':
    main()
