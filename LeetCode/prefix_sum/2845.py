class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        remainder_map = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            if num % modulo == k:
                prefix += 1

            current = prefix % modulo
            target = (current - k) % modulo

            if target in remainder_map:
                answer += remainder_map[target]

            remainder_map[current] = remainder_map.get(current, 0) + 1

        return answer
