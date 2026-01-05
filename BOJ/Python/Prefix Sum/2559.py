import sys


def main():
    input = sys.stdin.readline

    N, K = map(int, input().split())
    temps = list(map(int, input().split()))

    window_sum = sum(temps[:K])
    max_temp = window_sum

    for i in range(K, N):
        window_sum += (temps[i] - temps[i-K])

        max_temp = max(max_temp, window_sum)

    print(max_temp)


if __name__ == '__main__':
    main()
