class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = [num for num in nums if num != 0]
        heapq.heapify(heap)

        count = 0
        while sum(heap):
            pop_value = heapq.heappop(heap)
            heap = [num - pop_value for num in heap if num - pop_value != 0]
            heapq.heapify(heap)

            count += 1
        
        return count
