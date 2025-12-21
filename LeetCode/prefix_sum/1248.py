class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [num%2 for num in nums]

        prefix_count = {0: 1}
        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_count:
                answer += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return answer
