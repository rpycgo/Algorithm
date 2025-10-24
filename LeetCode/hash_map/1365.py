class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hashmap = {}

        for i, num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num] = i

        answer = [hashmap[num] for num in nums]

        return answer
