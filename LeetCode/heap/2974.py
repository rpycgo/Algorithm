class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        results = []

        while nums:
            first_biggest_value = heapq.heappop(nums)
            second_biggest_value = heapq.heappop(nums)

            results.extend([second_biggest_value, first_biggest_value])
        
        return results
