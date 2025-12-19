class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_sum = nums[:]
        for i in range(1, n-1):
            left_sum[i] += left_sum[i-1]

        left_sum = [0] + left_sum[:-1]

        right_sum = nums[:]
        right_sum[0] = sum(nums) - nums[0]
        for i in range(1, n):
            right_sum[i] = right_sum[i-1]  - right_sum[i]

        answer = [abs(left - right) for left, right in zip(left_sum, right_sum)]

        return answer
