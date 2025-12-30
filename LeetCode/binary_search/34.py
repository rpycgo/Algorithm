class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        idx_left = bisect_left(nums, target)
        idx_right = bisect_right(nums, target) - 1

        if idx_left < len(nums) and nums[idx_left] == target:
            answer = [idx_left, idx_right]
        else:
            answer = [-1, -1]

        return answer
