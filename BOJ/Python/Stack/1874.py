import sys


def main():
    input = sys.stdin.readline

    n = int(input())
    stack = []
    answer = []
    current = 1
    possible = True

    for _ in range(n):
        target = int(input())

        while current <= target:
            stack.append(current)
            answer.append('+')
            current += 1

        if stack[-1] == target:
            stack.pop()
            answer.append('-')
        else:
            possible = False
            break

    answer = '\n'.join(answer) if possible else 'NO'

    print(answer)


if __name__ == '__main__':
    main()
