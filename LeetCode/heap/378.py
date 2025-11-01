class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        size = len(matrix) ** 2

        heap = []
        for row in matrix:
            for element in row:
                heapq.heappush(heap, -element)

                if len(heap) > k:
                    heapq.heappop(heap)

        return -heap[0]
