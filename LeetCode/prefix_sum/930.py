class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = {0: 1}
        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in prefix_count:
                answer += prefix_count[prefix_sum - goal]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return answer
