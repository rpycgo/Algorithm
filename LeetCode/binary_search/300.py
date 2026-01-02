class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            if not tails or tails[-1] < num:
                tails.append(num)
            else:
                idx = bisect_left(tails, num)
                tails[idx] = num

        answer = len(tails)

        return answer
