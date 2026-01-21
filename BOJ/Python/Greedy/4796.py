import sys


input = sys.stdin.readline


def main():
    i = 1
    while True:
        L, P, V = map(int, input().split())

        if L == 0 and P == 0 and V == 0:
            return

        quotient, remainder = divmod(V, P)
        answer = L*quotient + min(remainder, L)
        print(f'Case {i}: {answer}')

        i += 1


if __name__ == '__main__':
    main()
