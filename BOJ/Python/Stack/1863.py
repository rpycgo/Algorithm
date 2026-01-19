import sys


input = sys.stdin.readline


def main():
    N = int(input())

    stack = []
    cnt = 0

    for _ in range(N):
        _, y = map(int, input().split())

        while stack and stack[-1] > y:
            stack.pop()
            cnt += 1

        if y > 0 and (not stack or stack[-1] < y):
            stack.append(y)

    cnt += len(stack)
    print(cnt)


if __name__ == '__main__':
    main()
