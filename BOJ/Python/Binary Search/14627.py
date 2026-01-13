import sys


def calculate_n_green_onion_chicken(amount, array):
    count = 0
    for length in array:
        count += length // amount

    return count


def main():
    input = sys.stdin.readline

    S, C = map(int, input().split())
    L = [int(input()) for _ in range(S)]

    left = 1
    right = max(L)

    length = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_n_green_onion_chicken(mid, L) >= C:
            length = mid
            left = mid + 1
        else:
            right = mid - 1

    total_length = sum(L)
    answer = total_length - (length*C)

    print(answer)


if __name__ == '__main__':
    main()
