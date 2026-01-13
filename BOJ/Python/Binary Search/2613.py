import sys


def is_group_less_than_M(limit, M, nums):
    cnt = 1
    total = 0

    for num in nums:
        if total + num > limit:
            cnt += 1
            total = num
        else:
            total += num

    return cnt <= M


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    left = max(nums)
    right = sum(nums)

    limit = right
    while left <= right:
        mid = (left+right) // 2

        cnt = 1
        total = 0
        for num in nums:
            if total + num > mid:
                cnt += 1
                total = num
            else:
                total += num

        if is_group_less_than_M(mid, M, nums):
            limit = mid
            right = mid -1
        else:
            left = mid + 1

    answer = []
    total = 0
    cnt = 0

    for i, num in enumerate(nums):
        total += num
        cnt += 1

        remaining_nums = N - (i+1)
        remaining_groups = M - (len(answer)+1)

        if (i+1 < N and total+nums[i+1] > limit) or (remaining_nums == remaining_groups):
            answer.append(cnt)
            total = 0
            cnt = 0

    print(limit)
    print(*answer)


if __name__ == '__main__':
    main()
