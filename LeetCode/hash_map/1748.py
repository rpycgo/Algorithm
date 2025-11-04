class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        answer = sum([key for key, value in count.items() if value == 1])

        return answer
