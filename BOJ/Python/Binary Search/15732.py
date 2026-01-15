import sys


input = sys.stdin.readline


def get_boxes(max_box_num, rules):
    count = 0
    for start, end, interval in rules:
        limit = min(end, max_box_num)

        if limit >= start:
            count += (limit - start) // interval + 1

    return count


def main():
    N, K, D = map(int, input().split())

    rules = [
        list(map(int, input().split()))
        for _
        in range(K)
    ]

    left = 1
    right = N

    answer = right
    while left <= right:
        mid = (left + right) // 2

        if get_boxes(mid, rules) >= D:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)


if __name__ == '__main__':
    main()
