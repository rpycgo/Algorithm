class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        answer = [key for key, value in count.items() if value == 2]
        answer.sort()

        return answer
