import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    expressions = input().rstrip()
    numbers = [int(input()) for _ in range(N)]

    stack = []
    for char in expressions:
        if char.isalpha():
            stack.append(numbers[ord(char) - ord('A')])
        else:
            right = stack.pop()
            left = stack.pop()

            if char == '+':
                stack.append(left + right)
            elif char == '-':
                stack.append(left - right)
            elif char == '*':
                stack.append(left * right)
            elif char == '/':
                stack.append(left / right)

    print(f'{stack[0]:.2f}')


if __name__ == '__main__':
    main()
