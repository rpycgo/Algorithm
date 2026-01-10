import sys


def main():
    input = sys.stdin.readline

    stack = []
    answer = 0
    temp = 1

    string = input().rstrip()
    for i, char in enumerate(string):
        if char == '(':
            stack.append('(')
            temp *= 2
        elif char == '[':
            stack.append('[')
            temp *= 3
        elif char == ')':
            if not stack or stack[-1] == '[':
                print(0)
                return

            if string[i-1] == '(':
                answer += temp

            stack.pop()
            temp //= 2
        elif char == ']':
            if not stack or stack[-1] == '(':
                print(0)
                return

            if string[i-1] == '[':
                answer += temp

            stack.pop()
            temp //= 3

    if stack:
        print(0)
    else:
        print(answer)


if __name__ == '__main__':
    main()
