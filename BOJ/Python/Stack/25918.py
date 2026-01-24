import sys


input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    if N%2 == 1:
        print(-1)
        return

    cnt = 0
    stack = []

    for char in S:
        if not stack or stack[-1] == char:
            stack.append(char)
        else:
            stack.pop()

        cnt = max(cnt, len(stack))

    answer = -1 if stack else cnt
    print(answer)


if __name__ == '__main__':
    main()
