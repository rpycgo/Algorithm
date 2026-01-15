import sys


input = sys.stdin.readline


def calculate_n_groups(target, scores):
    count = 0

    curr_sum = 0
    for score in scores:
        curr_sum += score

        if curr_sum >= target:
            curr_sum = 0
            count += 1

    return count


def main():
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    left = 1
    right = sum(scores)

    answer = right
    while left <= right:
        mid = (left+right) // 2

        if calculate_n_groups(mid, scores) >= K:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == '__main__':
    main()
