import sys


input = sys.stdin.readline


def main():
    MAX = 1_000_000

    f = [0] * (MAX + 1)
    for i in range(1, MAX+1):
        for j in range(i, MAX+1, i):
            f[j] += i

    g = [0] * (MAX + 1)
    for i in range(1, MAX+1):
        g[i] = g[i-1] + f[i]


    T = int(input())
    for _ in range(T):
        N = int(input())

        result = g[N]
        print(result)


if __name__ == '__main__':
    main()
