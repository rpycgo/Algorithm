import sys


input = sys.stdin.readline


def calculate_n_balloon(n_balloon, A):
    count = 0
    for a in A:
        count += (n_balloon // a)

    return count


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    left = 1
    right = min(A) * M

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_n_balloon(mid, A) >= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
