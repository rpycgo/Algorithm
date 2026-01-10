import sys


def main():
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        left = []
        right = []

        password = input().strip()
        for char in password:
            if char == '<':
                if left:
                    right.append(left.pop())
            elif char == '>':
                if right:
                    left.append(right.pop())
            elif char == '-':
                if left:
                    left.pop()
            else:
                left.append(char)

        answer = ''.join(left) + ''.join(right[::-1])

        print(answer)


if __name__ == '__main__':
    main()
