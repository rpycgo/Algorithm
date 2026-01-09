import sys


def main():
    input = sys.stdin.readline

    stack = []
    N = int(input())
    for _ in range(N):
        command = input().split()
        operation = command[0]

        if operation == 'push':
            val = command[1]

            stack.append(val)
        else:
            if operation == 'top':
                print(stack[-1] if stack else -1)
            elif operation == 'size':
                print(len(stack))
            elif operation == 'empty':
                print(0 if stack else 1)
            elif operation == 'pop':
                if not stack:
                    print(-1)
                    continue

                val = stack.pop()

                print(val)


if __name__ == '__main__':
    main()
