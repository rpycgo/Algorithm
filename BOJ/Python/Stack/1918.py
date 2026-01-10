import sys


def main():
    input = sys.stdin.readline

    expression = input().rstrip()

    stack = []
    result = ''

    priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    for char in expression:
        if char.isalpha():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()

            stack.pop()
        else:
            while stack and priority[stack[-1]] >= priority[char]:
                result += stack.pop()

            stack.append(char)

    while stack:
        result += stack.pop()

    print(result)


if __name__ == '__main__':
    main()
