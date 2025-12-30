class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0

        for i, num in enumerate(nums):
            idx = bisect_left(nums, target - num, i+1)

            answer += (idx - (i+1))

        return answer
