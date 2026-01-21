import sys


input = sys.stdin.readline


def main():
    A, B = input().split()

    min_val = int(A.replace('6', '5')) + int(B.replace('6', '5'))
    max_val = int(A.replace('5', '6')) + int(B.replace('5', '6'))

    print(f'{min_val} {max_val}')


if __name__ == '__main__':
    main()
