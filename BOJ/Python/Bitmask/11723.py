import sys


def main():
    input = sys.stdin.readline

    M = int(input())

    S = 0
    for _ in range(M):
        command = input().split()

        operation = command[0]
        if operation == 'all':
            S = (1 << 21) - 1
        elif operation == 'empty':
            S = 0
        else:
            x = int(command[1])

            if operation == 'add':
                S |= (1 << x)
            elif operation == 'remove':
                S &= ~(1 << x)
            elif operation == 'check':
                print(1 if S & (1 << x) else 0)
            elif operation == 'toggle':
                S ^= (1 << x)


if __name__ == '__main__':
    main()
