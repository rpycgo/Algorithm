class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = (set(range(1, len(nums)+1)) - seen).pop()

        answer = [duplicate, missing]

        return answer
