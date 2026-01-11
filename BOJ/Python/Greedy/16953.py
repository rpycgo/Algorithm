import sys


def main():
    input = sys.stdin.readline

    A, B = map(int, input().split())

    answer = 1
    while A < B:
        if B%2 == 0:
            B //= 2
        elif B%10 == 1:
            B //= 10
        else:
            break

        answer += 1

    answer = answer if A == B else -1

    print(answer)


if __name__ == '__main__':
    main()
