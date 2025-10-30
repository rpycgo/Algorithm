class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        n = len(nums)
        for num in range(1, n+1):
            count[num] += 1

        for num in nums:
            count[num] -= 1

        answer = [key for key, value in count.items() if value == 1]

        return answer
