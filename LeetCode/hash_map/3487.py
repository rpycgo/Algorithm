class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        max_num = float('-inf')
        positive_sum = 0
        for num in unique_nums:
            if num > 0:
                positive_sum += num
            if num > max_num:
                max_num = num

        answer = positive_sum if positive_sum > 0 else max_num

        return answer
