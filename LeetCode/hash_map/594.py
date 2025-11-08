class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        longest_harmonious_subsequences = 0
        for key in count:
            if (key+1 in count and key in count)\
                and count[key+1] + count[key] > longest_harmonious_subsequences:
                longest_harmonious_subsequences = count[key+1] + count[key]

        return longest_harmonious_subsequences
