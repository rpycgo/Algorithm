import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    answer = 0
    stack = []

    for _ in range(N):
        h = int(input())

        while stack and stack[-1] <= h:
            stack.pop()

        answer += len(stack)

        stack.append(h)

    print(answer)


if __name__ == '__main__':
    main()
