class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        min_value = min(nums)
        if min_value < 0:
            min_value = abs(min_value)
            nums = [num + min_value for num in nums]

        count = [0] * (max(nums) + 1)
        for num in nums:
            count[num] += 1

        max_consecutive = 1
        n_consecutive = 1
        for i in range(max(nums)):
            if count[i] and count[i+1]:
                n_consecutive += 1
            else:
                n_consecutive = 1

            if max_consecutive < n_consecutive:
                max_consecutive = n_consecutive

        return max_consecutive
