import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()

    stack = []

    for char in string:
        if not stack:
            stack.append(char)
            continue

        if char==')' and stack[-1]=='(':
            stack.pop()
            continue

        stack.append(char)

    cnt = len(stack)
    print(cnt)


if __name__ == '__main__':
    main()
