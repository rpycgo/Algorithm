import sys


input = sys.stdin.readline


def main():
    A = list(input().rstrip())
    T = input().rstrip()

    len_a = len(A)
    reverse_a = A[::-1]

    left_stack = []
    right_stack = []

    left, right = 0, len(T)-1

    while left <= right:
        while left <= right:
            left_stack.append(T[left])
            left += 1

            if len(left_stack) >= len_a and left_stack[-len_a:] == A:
                for _ in range(len_a):
                    left_stack.pop()
                break

        while left <= right:
            right_stack.append(T[right])
            right -= 1

            if len(right_stack) >= len_a and right_stack[-len_a:] == reverse_a:
                for _ in range(len_a):
                    right_stack.pop()
                break

    stack = left_stack + right_stack[::-1]

    answer = []
    for char in stack:
        answer.append(char)

        if len(answer) >= len_a and answer[-len_a:] == A:
            for _ in range(len_a):
                answer.pop()

    answer = ''.join(answer)
    print(answer)


if __name__ == '__main__':
    main()
