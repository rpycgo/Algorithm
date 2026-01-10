import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    numbers = list(map(int, input().split()))

    curr_num = 1
    stack = []

    for number in numbers:
        stack.append(number)

        while stack and stack[-1] == curr_num:
            stack.pop()

            curr_num += 1

    while stack and stack[-1] == curr_num:
        stack.pop()

        curr_num += 1

    answer = 'Sad' if stack else 'Nice'

    print(answer)


if __name__ == '__main__':
    main()
