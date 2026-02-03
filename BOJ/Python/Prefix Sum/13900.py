import sys


input = sys.stdin.readline


def main():
    N = int(input())
    nums = tuple(map(int, input().split()))

    total = sum(nums)

    answer = 0
    for num in nums:
        total -= num
        answer += (num * total)

    print(answer)


if __name__ == '__main__':
    main()
