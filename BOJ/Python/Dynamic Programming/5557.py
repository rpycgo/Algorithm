import sys


input = sys.stdin.readline


def solve(idx, curr_sum, target, nums, dp):
    if curr_sum < 0 or curr_sum > 20:
        return 0

    if idx == len(nums)-1:
        return 1 if curr_sum == target else 0

    if dp[idx][curr_sum] != -1:
        return dp[idx][curr_sum]

    cnt = 0
    cnt += solve(idx+1, curr_sum+nums[idx+1], target, nums, dp)
    cnt += solve(idx+1, curr_sum-nums[idx+1], target, nums, dp)

    dp[idx][curr_sum] = cnt

    return cnt


def main():
    N = int(input())
    nums = tuple(map(int, input().split()))

    target = nums[-1]
    nums = nums[:-1]

    dp = [[-1] * 21 for _ in range(N)]

    cnt = solve(0, nums[0], target, nums, dp)
    print(cnt)


if __name__ == '__main__':
    main()
