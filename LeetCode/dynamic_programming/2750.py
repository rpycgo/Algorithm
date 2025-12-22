class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        modulo = 10**9 + 7

        ones = [i for i, v in enumerate(nums) if v == 1]
        if not ones:
            return 0

        answer = 1
        for i in range(1, len(ones)):
            answer = answer * (ones[i] - ones[i-1]) % modulo

        return answer
