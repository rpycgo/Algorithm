import sys


def main():
    input = sys.stdin.readline

    stack = []
    K = int(input())

    for _ in range(K):
        val = int(input())

        if val == 0:
            stack.pop()
            continue

        stack.append(val)

    answer = sum(stack)
    print(answer)


if __name__ == '__main__':
    main()
