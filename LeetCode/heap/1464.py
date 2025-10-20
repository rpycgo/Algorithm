class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        first_biggest_value = heapq.heappop(nums)
        second_biggest_value = heapq.heappop(nums)

        return (first_biggest_value+1) * (second_biggest_value+1)
