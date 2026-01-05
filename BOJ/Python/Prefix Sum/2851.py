import sys


def main():
    input = sys.stdin.readline

    mashrooms = [int(input()) for _ in range(10)]

    prefix_sum = 0
    answer = 0
    min_diff = float('inf')

    for i in range(10):
        prefix_sum += mashrooms[i]
        diff = abs(prefix_sum - 100)

        if diff < min_diff or (diff == min_diff and prefix_sum > answer):
            min_diff = diff
            answer = prefix_sum

        if prefix_sum >= 100:
            break

    print(answer)


if __name__ == '__main__':
    main()
