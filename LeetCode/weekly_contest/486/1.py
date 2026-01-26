class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        split_idx = 0
        idx = 1
        prev_num = nums[0]

        while idx < len(nums):
            if prev_num >= nums[idx]:
                split_idx = idx

            prev_num = nums[idx]
            idx += 1

        return split_idx
