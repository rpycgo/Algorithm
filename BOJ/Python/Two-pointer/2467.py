import sys


def main():
    input = sys.stdin.readline

    N = int(input())
    liquids = list(map(int, input().split()))

    left = 0
    right = N - 1

    answer = float('inf')
    while left < right:
        mid = liquids[left] + liquids[right]

        if abs(mid) < abs(answer):
            answer = mid
            answer_left = liquids[left]
            answer_right = liquids[right]

        if mid < 0:
            left += 1
        else:
            right -= 1

    print(answer_left, answer_right)


if __name__ == '__main__':
    main()
