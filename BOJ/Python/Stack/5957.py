import sys


input = sys.stdin.readline


def main():
    N = int(input())

    dirties = list(range(N, 0, -1))
    washed = []
    dried = []

    while True:
        line = input().split()
        if not line:
            break

        cmd, num = map(int, line)

        if cmd == 1:
            for _ in range(num):
                if dirties:
                    washed.append(dirties.pop())
        else:
            for _ in range(num):
                if washed:
                    dried.append(washed.pop())

    for i in range(len(dried)-1, -1, -1):
        print(dried[i])


if __name__ == '__main__':
    main()
