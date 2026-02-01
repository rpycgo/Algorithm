import sys


input = sys.stdin.readline


def main():
    n = int(input())

    stack = []
    total_cost = 0

    for _ in range(n):
        num = int(input())

        if not stack:
            stack.append(num)
            continue

        if stack[-1] < num:
            total_cost += (num - stack[-1])

            while stack and stack[-1] <= num:
                stack.pop()
            stack.append(num)
        elif stack[-1] > num:
            stack.append(num)

    while len(stack) > 1:
        top = stack.pop()
        total_cost += (stack[-1] - top)

    print(total_cost)


if __name__ == '__main__':
    main()
