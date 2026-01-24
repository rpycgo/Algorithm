import sys


input = sys.stdin.readline


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    max_val = max(A)

    stack = []
    cnt = 0

    for num in A:
        if not stack:
            stack.append(num)
            continue

        if stack[-1] == num:
            continue
        elif stack[-1] > num:
            stack.pop()
            stack.append(num)
        else:
            cnt += (num - stack[-1])
            stack.pop()
            stack.append(num)

    if stack:
        cnt += (max_val - stack[0])

    print(cnt)


if __name__ == '__main__':
    main()
