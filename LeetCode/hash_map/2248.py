class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)

        for row in nums:
            for num in row:
                count[num] += 1

        answer = [key for key, value in count.items() if value == len(nums)]

        answer.sort()

        return answer
