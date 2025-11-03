class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse=True)

        answer = nums[:k]

        return answer
