class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(2, n):
            for j in range(i-1):
                target = nums[i] - nums[j]

                idx = bisect_left(nums, target+1, j+1, i)
                count += (i - idx)

        return count
