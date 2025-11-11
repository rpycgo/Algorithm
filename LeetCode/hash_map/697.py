class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        maximum_value = max(count.values())
        maximum_keys = [key for key, value in count.items() if value == maximum_value]

        answer = float('inf')
        for maximum_key in maximum_keys:
            if len(nums)-nums[::-1].index(maximum_key)-1 - nums.index(maximum_key) < answer:
                answer = len(nums)-nums[::-1].index(maximum_key)-1 - nums.index(maximum_key) + 1

        return answer
