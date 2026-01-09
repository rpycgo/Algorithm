import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    answer = [-1] * N
    stack = []

    for i, a in enumerate(A):
        while stack and A[stack[-1]] < a:
            idx = stack.pop()
            answer[idx] = a

        stack.append(i)

    print(*answer)


if __name__ == '__main__':
    main()
