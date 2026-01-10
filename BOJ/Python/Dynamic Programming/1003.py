import sys


def main():
    input = sys.stdin.readline

    T = int(input())

    zeros = [0] * 41
    ones = [0] * 41

    zeros[0] = 1
    zeros[1] = 0

    ones[0] = 0
    ones[1] = 1

    for i in range(2, 41):
        zeros[i] = zeros[i-1] + zeros[i-2]
        ones[i] = ones[i-1] + ones[i-2]

    for _ in range(T):
        n = int(input())
        print(f'{zeros[n]} {ones[n]}')


if __name__ == '__main__':
    main()
