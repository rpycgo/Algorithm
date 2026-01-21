import sys


input = sys.stdin.readline


def main():
    K = int(input())

    dp_A = [0] * K
    dp_B = [0] * K

    dp_A[0] = 0
    dp_B[0] = 1

    for i in range(1, K):
        dp_A[i] = dp_B[i-1]
        dp_B[i] = dp_B[i-1] + dp_A[i-1]

    print(f'{dp_A[K-1]} {dp_B[K-1]}')


if __name__ == '__main__':
    main()
