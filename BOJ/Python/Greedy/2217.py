import sys


input = sys.stdin.readline


def main():
    N = int(input())
    ropes = [int(input()) for _ in range(N)]
    ropes.sort(reverse=True)

    max_weight = 0
    for i in range(N):
        curr_weight = ropes[i] * (i + 1)

        max_weight = max(max_weight, curr_weight)

    print(max_weight)


if __name__ == '__main__':
    main()
