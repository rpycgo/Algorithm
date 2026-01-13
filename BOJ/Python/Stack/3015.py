import sys


def main():
    input = sys.stdin.readline

    N = int(input())

    answer = 0
    stack = []

    for _ in range(N):
        h = int(input())

        while stack and stack[-1][0] < h:
            answer += stack.pop()[1]

        if not stack:
            stack.append((h, 1))
            continue

        if stack[-1][0] == h:
            count = stack.pop()[1]
            answer += count

            if stack:
                answer += 1

            stack.append((h, count+1))
        else:
            answer += 1
            stack.append((h, 1))

    print(answer)


if __name__ == '__main__':
    main()
