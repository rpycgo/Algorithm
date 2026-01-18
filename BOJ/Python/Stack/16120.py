import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()

    stack = []
    for char in string:
        stack.append(char)

        if len(stack) >= 4:
            if ''.join(stack[-4:]) == 'PPAP':
                for _ in range(4):
                    stack.pop()
                stack.append('P')

    answer = 'PPAP' if stack == ['P'] else 'NP'
    print(answer)


if __name__ == '__main__':
    main()
