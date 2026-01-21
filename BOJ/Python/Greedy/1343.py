import sys


input = sys.stdin.readline


def main():
    board = input().rstrip()

    board = board.replace('XXXX', 'AAAA')
    board = board.replace('XX', 'BB')

    answer = -1 if 'X' in board else board
    print(answer)


if __name__ == '__main__':
    main()
