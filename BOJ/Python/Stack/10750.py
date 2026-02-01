import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()
    substring = list(input().rstrip())

    len_substring = len(substring)
    left, right = 0, len(string)-1

    stack = []
    while left <= right:
        stack.append(string[left])

        while len(stack) >= len_substring and stack[-len_substring:] == substring:
            for _ in range(len_substring):
                stack.pop()

        left += 1

    answer = ''.join(stack)
    print(answer)


if __name__ == '__main__':
    main()
