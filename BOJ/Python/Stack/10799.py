import sys


def main():
    input = sys.stdin.readline

    data = input().rstrip()

    stack = []

    answer = 0
    for i, char in enumerate(data):
        if char == '(':
            stack.append(char)
        else:
            stack.pop()

            if data[i-1] == '(':
                answer += len(stack)
            else:
                answer += 1

    print(answer)


if __name__ == '__main__':
    main()
