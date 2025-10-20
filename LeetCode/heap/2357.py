class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = [num for num in nums if num != 0]

        heapq.heapify(heap)
        count = 0
        previous = 0

        while heap:
            pop_value = heapq.heappop(heap)

            if pop_value > previous:
                previous = pop_value

                count += 1

        return count
