import sys


input = sys.stdin.readline


def main():
    i = 1
    while True:
        string = input().rstrip()

        if '-' in string:
            break

        stack = []
        cnt = 0

        for char in string:
            if char == '{':
                stack.append('{')
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(char)

        while stack:
            char1 = stack.pop()
            char2 = stack.pop()

            if char1 == char2:
                cnt += 1
            else:
                cnt += 2

        print(f'{i}. {cnt}')

        i += 1

if __name__ == '__main__':
    main()
