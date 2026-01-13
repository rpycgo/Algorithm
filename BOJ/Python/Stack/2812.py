import sys


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    number = input().rstrip()

    stack = []
    to_remove = K

    for digit in number:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    answer = stack[:-to_remove] if to_remove else stack
    answer = ''.join(answer)

    print(answer)


if __name__ == '__main__':
    main()
