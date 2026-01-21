import sys


input = sys.stdin.readline


def main():
    string = input().rstrip()

    n_zeros = 0
    n_ones = 0

    if string[0] == '0':
        n_zeros += 1
    else:
        n_ones += 1

    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            if string[i] == '0':
                n_zeros += 1
            else:
                n_ones += 1

    answer = min(n_zeros, n_ones)
    print(answer)


if __name__ == '__main__':
    main()
