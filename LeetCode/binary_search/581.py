class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start = -1
        end = -2

        min_val = nums[-1]
        max_val = nums[0]

        for i in range(1, n):
            max_val = max(max_val, nums[i])

            if nums[i] < max_val:
                end = i

            j = n - 1 - i
            min_val = min(min_val, nums[j])

            if nums[j] > min_val:
                start = j

        answer = end - start + 1

        return answer
