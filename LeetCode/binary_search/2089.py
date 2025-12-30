class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        left_idx = bisect_left(nums, target)
        right_idx = bisect_right(nums, target)

        answer = list(range(left_idx, right_idx))

        return answer
