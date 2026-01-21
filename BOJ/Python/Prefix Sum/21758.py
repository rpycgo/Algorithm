import sys


input = sys.stdin.readline


def main():
    N = int(input())
    honeys = tuple(map(int, input().split()))

    prefix_sum = [0] * N
    prefix_sum[0] = honeys[0]

    for i in range(1, len(honeys)):
        prefix_sum[i] = prefix_sum[i-1] + honeys[i]

    total = prefix_sum[N-1]
    answer = 0

    for i in range(1, N-1):
        val = (total-honeys[0]-honeys[i]) + (total-prefix_sum[i])
        answer = max(answer, val)

    for i in range(1, N-1):
        val = (total-honeys[N-1]-honeys[i]) + (prefix_sum[i-1])
        answer = max(answer, val)

    for i in range(1, N-1):
        val = (prefix_sum[i]-honeys[0]) + (total-prefix_sum[i-1]-honeys[N-1])
        answer = max(answer, val)

    print(answer)


if __name__ == '__main__':
    main()
