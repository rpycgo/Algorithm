class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if num == 0 else num for num in nums]

        prefix_count = {0: -1}
        prefix_sum = 0
        answer = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum in prefix_count:
                answer = max(answer, i - prefix_count[prefix_sum])
            else:
                prefix_count[prefix_sum] = i

        return answer
