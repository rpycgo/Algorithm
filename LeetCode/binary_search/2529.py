class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        n_negative = bisect_left(nums, 0)
        n_positive = n - bisect_left(nums, 1)

        answer = max(n_negative, n_positive)

        return answer
