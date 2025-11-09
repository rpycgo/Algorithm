class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)-1):
            for j in range(1, len(arr)):
                heapq.heappush(heap, (-arr[i]/arr[j], arr[i], arr[j]))

                if len(heap) > k:
                    heapq.heappop(heap)

        answer = heap[0][1:]

        return answer
