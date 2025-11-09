class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        nums.sort()

        maximum_total_value = nums[-1] - nums[0]
        answer = maximum_total_value * k

        return answer
