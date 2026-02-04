import sys


input = sys.stdin.readline


def main():
    pair = {')': '(', ']': '[', '}': '{'}

    while True:
        string = input().rstrip()

        if string == '#':
            break

        stack = []
        for char in string:
            if char in {'(', '[', '{'}:
                stack.append(char)
            elif char in {')', ']', '}'}:
                if stack and stack[-1] == pair.get(char):
                    stack.pop()
                else:
                    stack.append(char)

        answer = 'Legal' if not stack else 'Illegal'
        print(answer)


if __name__ == '__main__':
    main()
