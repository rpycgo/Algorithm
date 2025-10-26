class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        largest_value = -1

        for num in nums:
            if -num in nums:
                if abs(num) > largest_value:
                    largest_value = abs(num)

        return largest_value
