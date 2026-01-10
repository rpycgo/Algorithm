import sys


def main():
    input = sys.stdin.readline

    answer = 0

    N = int(input())
    for _ in range(N):
        string = input().rstrip()

        stack = []
        for char in string:
            if not stack:
                stack.append(char)
                continue

            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        is_good = 0 if stack else 1
        answer += is_good

    print(answer)


if __name__ == '__main__':
    main()
