import sys


input = sys.stdin.readline


def main():
    n = int(input())
    parenthesis = input().rstrip()

    stack = [-1]
    max_len = 0

    for i in range(n):
        if parenthesis[i] == '(':
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    print(max_len)


if __name__ == '__main__':
    main()
