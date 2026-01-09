import sys


def main():
    input = sys.stdin.readline

    mapping = {']': '[', ')': '('}

    while True:
        line = input().rstrip('\n')

        if line == '.':
            break

        stack = []
        is_balanced = True

        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')' or char == ']':
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    is_balanced = False
                    break

        answer = 'yes' if is_balanced and not stack else 'no'

        print(answer)


if __name__ == '__main__':
    main()
