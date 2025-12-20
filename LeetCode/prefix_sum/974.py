class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = {0: 1}
        answer = 0

        running_sum = 0
        for num in nums:
            running_sum += num
            running_sum %= k

            if running_sum in remainder_map:
                answer += remainder_map[running_sum]

            remainder_map[running_sum] = remainder_map.get(running_sum, 0) + 1

        return answer
