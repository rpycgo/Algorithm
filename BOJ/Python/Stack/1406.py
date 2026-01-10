import sys


def main():
    input = sys.stdin.readline

    string = input().rstrip()

    left = list(string)
    right = []

    M = int(input())
    for _ in range(M):
        operations = input().split()

        if operations[0] == 'L':
            if left:
                right.append(left.pop())
        elif operations[0] == 'D':
            if right:
                left.append(right.pop())
        elif operations[0] == 'B':
            if left:
                left.pop()
        elif operations[0] == 'P':
            left.append(operations[1])

    answer = ''.join(left) + ''.join(right[::-1])

    print(answer)


if __name__ == '__main__':
    main()
