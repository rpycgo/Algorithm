class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        top_k_index = []
        for _ in range(k):
            top_k_index.append(heapq.heappop(heap)[1])

        top_k_index.sort()

        return [nums[i] for i in top_k_index]
