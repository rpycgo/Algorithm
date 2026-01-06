import sys


def calculate_total_pieces(length, snack_lengths):
    total_pieces = 0
    for snack_length in snack_lengths[::-1]:
        total_pieces += snack_length // length

        if snack_length < length:
            break

    return total_pieces


def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())
    snack_lengths = list(map(int, input().split()))
    snack_lengths.sort()

    left = 1
    right = max(snack_lengths)

    answer = 0
    while left <= right:
        mid = (left+right) // 2

        if mid == 0:
            break

        if calculate_total_pieces(mid, snack_lengths) >= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
