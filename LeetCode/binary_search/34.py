class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        idx_left = bisect_left(nums, target)
        idx_right = bisect_right(nums, target) - 1

        if idx_left < len(nums) and nums[idx_left] == target:
            pass
        else:
            idx_left = -1
        if nums[idx_right] != target:
            idx_right = -1    

        answer = [idx_left, idx_right]

        return answer
