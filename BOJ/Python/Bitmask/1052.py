import sys


input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    if N <= K:
        print(0)
        return

    answer = 0
    while bin(N).count('1') > K:
        low_bit = N & -N

        N += low_bit
        answer += low_bit

    print(answer)


if __name__ == '__main__':
    main()
