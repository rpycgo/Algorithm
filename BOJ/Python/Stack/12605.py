import sys
from collections import deque


input = sys.stdin.readline


def main():
    N = int(input())
    for i in range(N):
        string = input().rstrip().split()

        stack = deque([])
        for word in string:
            stack.appendleft(word)

        answer = ' '.join(stack)
        print(f'Case #{i+1}: {answer}')


if __name__ == '__main__':
    main()
