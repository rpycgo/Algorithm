import sys
from collections import Counter


def main():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    count = Counter(A)

    answer = [-1] * N
    stack = []

    for i, num in enumerate(A):
        while stack and count[A[stack[-1]]] < count[num]:
            idx = stack.pop()
            answer[idx] = num

        stack.append(i)

    print(*answer)


if __name__ == '__main__':
    main()
